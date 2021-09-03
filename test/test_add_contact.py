
from model.contact_class import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="1234", middlename="1243", lastname="234", nickname="324", title="324234",
                            company="fdge", address="ebebebt", home_number="4532532", mobile_number="5435435435",
                            work_number="234324", fax="12333", email="bteby56@mail.ru", email2="bteby56@mail.ru",
                            email3="bteby56@mail.ru", homepage="bteby56@mail.ru", bday="10", bmonth="November",
                            byear="1999", aday="12", amonth="December", ayear="2018", address2="greg3g43",
                            phone2="32g4", notes="vbfdbr"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                            company="", address="", home_number="", mobile_number="", work_number="", fax="",
                            email="", email2="", email3="", homepage="", bday="-", bmonth="-",
                            byear="", aday="-", amonth="-", ayear="", address2="", phone2="", notes=""))
    app.session.logout()
