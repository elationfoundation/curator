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


from flask import Flask, render_template
from curator import public, user
from curator.extensions import db, limiter
from curator.settings import ProdConfig

def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    limiter.init_app(app)
    return None

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    #app.register_blueprint(user.views.blueprint)
    return None
