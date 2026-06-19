from setuptools import setup, find_packages

setup(
    name="refusal-mapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["openai>=1.0", "click", "rich"],
    entry_points={"console_scripts": ["refusal-mapper=refusal_mapper.cli:main"]},
    python_requires=">=3.10",
)
