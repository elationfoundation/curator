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
from flask import current_app, render_template
from curator.models.bibliography import Work, WorkNotFoundError

blueprint = Blueprint('public', __name__, static_folder='../static')

@blueprint.route("/")
def home():
    return render_template('public/home.html')

@blueprint.route("/search")
def search():
    return render_template('public/search.html')

@blueprint.route("/view/<item_uuid>")
def view(item_uuid):
    item = Work.query.filter_by(uuid=item_uuid).first_or_404()
    return render_template('work.html', item=item)
