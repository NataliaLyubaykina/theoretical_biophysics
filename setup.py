from setuptools import setup

# Read the README file for the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="theoretical_biophysics",
    version="0.1.0",
    author="Natalia Lyubaykina",
    author_email="natalia.lyubaykina@gmail.com",
    description="A package for theoretical biophysics simulations and analyses, featuring examples from my PhD thesis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NataliaLyubaykina/theoretical_biophysics",
    packages=['theoretical_biophysics'],
    install_requires=[
        "numpy>=1.25.0",
        "matplotlib>=3.7.1",
        "tqdm>=4.66.1"
    ],
    license="MIT",
    python_requires='>=3.6',
)
