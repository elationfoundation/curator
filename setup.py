#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of curator
# Copyright © 2016 seamus tuohy, <s2e+code@seamustuohy.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the included LICENSE file for details.

from distutils.core import setup, find_packages

setup(name='curator',
      version='0.0.1',
      description='A linked resource viewer.',
      author='Seamus Tuohy',
      author_email='s2e+code@seamustuohy.com',
      url='https://github.com/elationfoundation/curator',
      packages=find_packages(exclude=['docs']),
      keywords='archive search',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Development Status :: 2 - Pre-Alpha',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3']
)
