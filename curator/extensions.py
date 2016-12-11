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

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# limiter = Limiter(
#     key_func=get_remote_address,
#     global_limits=["100 per day", "50 per hour"])
# #    exempt_when=lambda: current_user.is_authenticated))
