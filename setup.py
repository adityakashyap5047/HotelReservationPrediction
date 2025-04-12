from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel Reservation Prediction",
    version="0.1",
    author="Aditya Kumar",
    packages=find_packages(),
    install_requires=requirements,
    description="A package for predicting hotel reservation cancellations.",
)