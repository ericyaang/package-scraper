from setuptools import setup, find_packages

setup(
    author='Eric Yang',
    description='A template package for myself',
    name='scraper-olx',
    version='0.1.0',
    packages=find_packages(include=['scraper', 'scraper.*']),
    install_requires=['pandas','requests', 'datetime', 'IPython', 'BeautifulSoup'],
)