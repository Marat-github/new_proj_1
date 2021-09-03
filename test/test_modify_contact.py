from model.contact_class import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="FIRSTNAME", middlename="MIDDLENAME", lastname="LASTNAME", nickname="NICKNAME", title="TITLE",
                            company="COMPANY", address="ADDRESS", home_number="00000000", mobile_number="00000000",
                            work_number="0000000", fax="0000000", email="123456789@mail.ru", email2="123456789@mail.ru",
                            email3="123456789@mail.ru", homepage="123456789@mail.ru", bday="10", bmonth="November",
                            byear="1999", aday="10", amonth="November", ayear="1999", address2="address2",
                            phone2="0000000000", notes="NOTES"))
    app.session.logout()