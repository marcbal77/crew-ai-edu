from setuptools import setup, find_packages

setup(
    name="edu",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "edu=edu.main:run",
        ],
    },
    install_requires=[
        "langtrace-python-sdk",
        # add other dependencies here
    ],
)
