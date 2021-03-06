from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='npy4chan',
    version='0.1.0',
    description='A trivial, minimalistic 4chan API wrapper.',
    long_description=long_description,
    url='https://github.com/MineRobber9000/npy4chan',
    author='Robert Miles',
    author_email='milesrobert374@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='4chan imageboard API',
    packages=["npy4chan"],
    install_requires=['requests'],
)
