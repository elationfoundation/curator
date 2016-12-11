#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of curator
# Copyright © 2016 seamus tuohy, <code@seamustuohy.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the included LICENSE file for details.

import uuid
from curator.extensions import db
from curator.models.helpers import GUID


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(3), default='eng')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))

class UUID(db.Model):
    id = db.Column(GUID(), default=uuid.uuid4, nullable=False, unique=True, primary_key=True)
