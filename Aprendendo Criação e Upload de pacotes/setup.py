from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="adicao_subtracao",
    version="0.0.1",
    author="jonatas bernardes de oliveira",
    author_email="jonatas-bernardes@hotmail.com",
    description="Esse pacote faz soma e subtracao de dois números",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url= "https://github.com/jonatas177/Meu_Portfolio",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)