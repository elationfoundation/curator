#!/usr/bin/env bash
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

# Setup
set -euo pipefail

# TODO remove DEBUGGING
set -x

# Include
source install_helpers

main() {
    base_setup
    dependencies
    set_environment_vars
}

set_environment_vars() {
    # Store testing systems config values in the environment
    echo "CURATOR_DB_NAME=$CURATOR_DB_NAME" >> /etc/environment
    echo "CURATOR_DB_USER=$CURATOR_DB_USER" >> /etc/environment
    echo "CURATOR_DB_PASS=$CURATOR_DB_PASS" >> /etc/environment
    echo "CURATOR_DB_HOST=$CURATOR_DB_HOST" >> /etc/environment
    echo "CURATOR_DB_PORT=$CURATOR_DB_PORT" >> /etc/environment
    echo "CURATOR_FLASK_SECRET_KEY=$CURATOR_FLASK_SECRET_KEY" >> /etc/environment
    echo "CURATOR_FLASK_HAMC_KEY=$CURATOR_FLASK_HAMC_KEY" >> /etc/environment
    echo "CURATOR_KEYWORD_PATH=$CURATOR_KEYWORD_PATH" >> /etc/environment
    echo "CURATOR_REPORT_PATH=$CURATOR_REPORT_PATH" >> /etc/environment
}

base_setup() {
    apt-get update
}

dependencies() {

    apt_install "python3"
    apt_install "python3-pip"

    # Flask
    pip_install flask-security
    pip_install flask-sqlalchemy

    apt_install "git"
}

main
