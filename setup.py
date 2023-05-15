from setuptools import setup

setup(
    name="Models",
    version="1.0.0",
    description="Database models for Packstack",
    packages=['models'],
    install_requires=['jwt', 'passlib', 'sqlalchemy']
)
