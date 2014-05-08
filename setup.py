#!/usr/bin/env python

from pip.req import parse_requirements
from setuptools import setup
from subprocess import call

install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]
setup(
    name="Rubiz",
    version="0.1-alpha",
    install_requires=reqs
)

call("pip install -e git://github.com/benjiec/django-tables2-simplefilter.git#egg=django_tables2_simplefilter", shell=True)
