from setuptools import setup, find_packages

setup(
    name='okx_announcements_downloader',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4'],
)