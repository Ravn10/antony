# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
try: # for pip >= 10
	from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
	from pip.req import parse_requirements
import re, ast

# get version from __version__ variable in garage/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('garage/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

requirements = parse_requirements("requirements.txt", session="")

setup(
	name='garage',
	version=version,
	description='Keeps details of Vehicles , like chasis no, engine no, etc',
	author='crisco',
	author_email='support@criscoconsulting.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)