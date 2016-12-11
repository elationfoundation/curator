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

import os

class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('CURATOR_FLASK_SECRET_KEY')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    ASSETS_DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_HASH = 'bcrypt'
    # SECURITY_PASSWORD_SALT
    # https://github.com/mattupstate/flask-security/issues/135
    # It's actually used as the "KEY" to generate HAMC.
    # The password is hashed with HMAC and the SECURITY_PASSWORD_SALT
    # and then salted+encrypted by the passlib library.
    # for bcrypt the salt must be 22 characters long,
    # and drawn from the regexp range [./0-9A-Za-z]
    SECURITY_PASSWORD_SALT = os.environ.get('CURATOR_FLASK_HAMC_KEY')
    SQLALCHEMY_DATABASE_URI = get_database_adddress()

    def get_database_adddress():
    db_config = {"host": os.environ.get("CURATOR_DB_HOST"),
                 "user": os.environ.get("CURATOR_DB_USER"),
                 "password": os.environ.get("CURATOR_DB_PASS"),
                 "port": os.environ.get("CURATOR_DB_PORT"),
                 "name": os.environ.get("CURATOR_DB_NAME")}

    address = "postgresql://{user}:{password}/{host}:{port}/{name}".format(db_config)
    return address


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets

class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
