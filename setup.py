import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='today',
    version='0.0.1',
    install_requires=['tabulate>=0.8.2'],
    scripts=['bin/today'],
    author='Jay Vana',
    author_email='jaysvana@gmail.com',
    description='A utility built to keep track of things you are doing.',
    license='MIT',
    # packages=['today'],
    long_description=read('README.md'),
)
