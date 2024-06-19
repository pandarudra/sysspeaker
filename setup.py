from setuptools import setup, find_packages

setup(
    name="mymodule",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  
    author="rudra_826",
    author_email="rudrapanda8206@gmail.com",
    description="A simple example module",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/pandarudra/sysspeaker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
