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

from flask import current_app
from curator.extensions import db
from curator.models.metadata import Language, Tag, UUID

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('work_id', db.Integer, db.ForeignKey('work.id'))
)

class BF_Item(db.Model):
    """ The base bibliography model

    Based on the BIBFRAME vocabulary"""

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(256))
    source = db.Column(db.String(256))
    agent = db.Column(db.Integer)
    date  = db.Column(db.DateTime)
    note = db.Column(db.String(256))
    status = db.Column(db.String(256))
    content = db.Column(db.String(256))
    # ISO 639-2/T
    # Metadata
    creationDate  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    changeDate = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    language = db.Column(db.Integer, db.ForeignKey('language.id'))



class Work(BF_Item):
    summary = db.Column(db.String(256))
    subject = db.Column(db.String(256))
    natureOfContent = db.Column(db.String(256))
    tags = db.relationship('Tag', secondary=tags,
                           backref=db.backref('work', lazy='dynamic'))
    uuid = db.relationship('UUIDS',
                           backref=db.backref('item', uselist=False))


    def create(self, source, **alt_properties):
        self.source = source
        properties = ["title", "agent", "date", "note"
                      "status", "content", "language",
                      "creationDate", "changeDate",
                      "summary", "subject", "natureOfContent",
                      "tags"]
        for prop in properties:
            try:
                self.validate_prop(prop, alt_properties[prop])
                setattr(self, prop, alt_properties[prop])
            except ValueError as _e:
                # log.info("Tried to set invalid property {0} as {1}".format(alt_properties[prop], prop))
                raise ValueError(_e)
        uuid = UUID()
        self.uuid = uuid
        db.session.add(uuid)
        db.session.add(self)
        db.session.commit()

    def validate_prop(self, prop, value):
        print("TODO")
        pass





#WorkNotFoundError
