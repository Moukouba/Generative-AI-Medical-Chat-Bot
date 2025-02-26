from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

AUTHOR_USER_NAME = "Moukouba"
AUTHOR_EMAIL = "m_moukouba@yahoo.fr"


setup(
    name="Generative-AI-Medical-Chat-Bot",
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small chat bot for madical assistance.",
    long_description=long_description,
    packages=find_packages()
)