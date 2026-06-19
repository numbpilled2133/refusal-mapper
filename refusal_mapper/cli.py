"""refusal-mapper — map LLM refusal boundaries through semantic variation."""

import click
import json
from . import probe, variants


@click.command()
@click.argument("prompt")
@click.option("--variants", default=50, help="Number of semantic variants to generate")
@click.option("--model", default="gpt-4o", help="Model to probe")
@click.option("--output", default=None, help="Output file (stdout if omitted)")
def main(prompt, variants, model, output):
    """Probe an LLM's refusal boundary by generating semantic variants of PROMPT."""
    print(f"[*] probing {model} with base prompt: {prompt[:60]}...")
    print(f"[*] generating {variants} semantic variants...")

    var_list = variants.generate(prompt, count=variants)
    results = probe.batch(model, var_list)

    report = {
        "base_prompt": prompt,
        "model": model,
        "total_variants": len(results),
        "refusal_rate": sum(1 for r in results if r["refused"]) / len(results) if results else 0,
        "boundary_contours": probe.calculate_contours(results),
        "variants": results,
    }

    output_text = json.dumps(report, indent=2)
    if output:
        with open(output, "w") as f:
            f.write(output_text)
        print(f"[+] saved to {output}")
    else:
        print(output_text)


if __name__ == "__main__":
    main()
