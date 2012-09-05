import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='simplerpc',
    version='0.1.0',
    author='Kevin L. Mitchell',
    author_email='kevin.mitchell@rackspace.com',
    description="Simple RPC",
    license='Apache License (2.0)',
    py_modules=['simplerpc'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    url='https://github.com/klmitch/simplerpc',
    long_description=read('README.rst'),
    install_requires=[
        'eventlet',
        ],
    tests_require=[
        'mox',
        ],
    )
