# -*- coding: utf-8 -*-
"""
setup file for creating python package pjInvert
"""
from setuptools import setup
from setuptools import find_packages

setup(name='pjInvert',
      version='0.1',
      description='tools for solving geophysics inverse problems',
      url='https://github.com/nvoss12838/pjInvert.git',
      author='Nick Voss',
      author_email= 'nvoss@mail.usf.edu',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
