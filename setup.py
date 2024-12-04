
from setuptools import setup, find_packages
from setuptools.command.install import install

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="ShellArgParser",
    version="0.2.3",
    description="Simple tool to parse shell arguments using eval",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiswillbeyourgithub/ShellArgParser",
    packages=find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    keywords=["shell", "zsh", "bash", "arguments", "args", "kwargs", "parser", "tool"],
    python_requires=">=3.9",

    entry_points={
        'console_scripts': [
            'ShellArgParser=ShellArgParser.__init__:cli_launcher',
        ],
    },

    install_requires=[
        'fire >= 0.5.0',
    ],

)
