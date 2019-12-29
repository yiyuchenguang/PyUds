# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:52:35 2019

@author: levy.he
"""

'''
    packages=find_packages(where='pyuds', exclude=['sample',
                           'sample.*', 'GacDiagTest', 'DbMessage.*', 'DbMessage']),
    packages=['pyuds',
                'pyuds.PyUds',
                'pyuds.PyUds.vxlapi',
                'pyuds.Scripts',
                'pyuds.TestCase',
                'pyuds.TestCase.Report'
                ],
    packages=[  '.',
                'PyUds',
                'PyUds.vxlapi',
                'Scripts',
                'TestCase',
                'TestCase.Report'
              ],
'''
from setuptools import setup, find_packages

setup(
    name="pyuds",
    version="1.0.0",
    zip_safe=False,
    description="python uds testcase",
    long_description="python uds testcase",
    license="MIT Licence",

    url="http://test.com",
    author="levy.he",
    author_email="levy.he@gmail.com",
    packages=find_packages(include=['pyuds','pyuds.*']),
    package_data={'PyUds.bus.driver.vector': ['vxlapi_32bit.dll', 'vxlapi_64bit.dll']},
    platforms="any",
    install_requires=[],
    python_requires=">=3.6",
)
