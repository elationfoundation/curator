# -*- coding: utf-8 -*-

import os
from curator import factory

if __name__ == '__main__':
    #Start Admin Interface
    admin_port = int(os.environ.get("PORT", 8080))
    app = factory.create_app()
    app.run('0.0.0.0', port=admin_port)
