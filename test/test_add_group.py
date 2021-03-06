# -*- coding: utf-8 -*-
from model.group_class import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="123", header="123", footer="123"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="", header="", footer=""))
    app.session.logout()
