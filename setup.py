# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name='injector',
    version='0.1.0',
    description='Library for injecting tracers (or other things) into code easily.',

    url='https://github.com/pirogoeth/injector',
    author='Sean Johnson',
    author_email='sean.johnson@maio.me',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ],

    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    scripts=[],
    install_requires=[],
    include_package_data=True,

    test_suite='nose.collector',
    tests_require=[
        'nose',
        'coverage',
    ],
    zip_safe=True
)
