#!/usr/bin/env python3

from setuptools import setup

setup(
    name="autoscrum",
    version="0.3.0",
    description="AutoScrum Automatic Project Planner",
    long_description=open("README.md").read(),
    license="GLPv3",
    packages=["autoscrum"],
    package_data={
        "autoscrum": [
            "data/*.hbs"
        ]
    }
)
