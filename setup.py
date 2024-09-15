from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = ''
LONG_DESCRIPTION = ''

setup(
    name="oxford_dictionary",
    version=VERSION,
    author="ArisDev",
    packages=find_packages(),
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=["aiohttp", "fake-useragent", "requests"]
)