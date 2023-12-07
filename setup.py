from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in basecamp/__init__.py
from basecamp import __version__ as version

setup(
	name="basecamp",
	version=version,
	description="Basecamp",
	author="shyam",
	author_email="shyam@8848digital.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
