from model.group_class import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New GROUP", header="HEADER", footer="FOOTER"))
    app.session.logout()

