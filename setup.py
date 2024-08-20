from setuptools import setup, find_packages

setup(
    name="git_clone_python",
    version="0.1",
    description="A simple version control system inspired by Git.",
    author="Himalaya Gupta",
    author_email="himalaya.gupta3@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'git-clone=git_clone_python.cli:main',  # This line registers the command-line tool
        ],
    },
    install_requires=[],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
