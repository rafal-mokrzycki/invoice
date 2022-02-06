import datetime
import re
import csv
import pandas as pd

'''import pandas as pd
from django.db import models'''


class Owner:
    '''
    class Owner defines the owner of the program and issuer of all invoices
    '''

    OWNER_DATA = pd.read_csv("owner.csv")

    def __init__(self, owner_id=OWNER_DATA.owner_id[0],
                 owner_tax_number=OWNER_DATA.owner_tax_number[0],
                 owner_first_name=OWNER_DATA.owner_first_name[0],
                 owner_last_name=OWNER_DATA.owner_last_name[0],
                 owner_company_name=OWNER_DATA.owner_company_name[0],
                 owner_street=OWNER_DATA.owner_street[0],
                 owner_house_number=OWNER_DATA.owner_house_number[0],
                 owner_flat_number=OWNER_DATA.owner_flat_number[0],
                 owner_zip_code=OWNER_DATA.owner_zip_code[0],
                 owner_city=OWNER_DATA.owner_city[0],
                 owner_email=OWNER_DATA.owner_email[0],
                 owner_phone_number=OWNER_DATA.owner_phone_number[0],
                 login=OWNER_DATA.login[0],
                 password=OWNER_DATA.password[0]):
        self.owner_id = owner_id
        self.owner_tax_number = owner_tax_number
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.owner_company_name = owner_company_name
        self.owner_street = owner_street
        self.owner_house_number = owner_house_number
        self.owner_flat_number = owner_flat_number
        self.owner_zip_code = owner_zip_code
        self.owner_city = owner_city
        self.owner_email = owner_email
        self.owner_phone_number = owner_phone_number
        self.__login = login
        self.__password = password

    def __str__(self) -> object:

        '''
        shows Owner basic data
        '''

        return """
{} {}
{}
{} {} / {}
{} {}
tax number: {}
""".format(self.owner_first_name, self.owner_last_name, self.owner_company_name,
           self.owner_street, self.owner_house_number, self.owner_flat_number, self.owner_zip_code,
           self.owner_city, self.owner_tax_number
           )

    @property
    def login(self):

        '''
        returns login
        '''

        return self.__login

    @property
    def password(self):

        '''
        returns password
        '''

        return self.__password

    @password.setter
    def password(self, value):

        '''
        enables to set a new password
        '''
        x = 0
        while x < 3:
            my_password = input("Type in your password: ")
            if self.__password == my_password:
                while True:
                    new_password = input("Type in your new password: ")
                    if new_password == self.__password:
                        print("The new password should be different from the old one.")
                    else:
                        if not re.match(r'[A-Za-z0-9]{8,}', new_password):
                            print(
                                "Your password must have at least 8 characters. Use lowercase letters, uppercase letters and numbers.")
                        else:
                            self.__password = new_password
                            print("New password has been set.")
                            break
                break
            else:
                print("Sorry, password is incorrect. Try again.")
            x += 1
        else:
            print("Sorry, you typed an incorrect password 3 times.")

        return self.__password

    @password.deleter
    def password(self):

        '''
        deletes the password
        '''

        self.__password = None

    def change_data(self, OWNER_DATA=OWNER_DATA):

        """
        enables to change any owner data except for login or password
        """

        print("""OWNER DATA:
{}:\t\t\t\t{}
{}:\t\t{}
{}:\t\t{}
{}:\t\t{}
{}:\t\t{}
{}:\t\t\t{}
{}:\t\t{}
{}:\t\t{}
{}:\t\t\t{}
{}:\t\t\t\t{}
{}:\t\t\t{}
{}:\t\t{}""".format(OWNER_DATA.columns[0], OWNER_DATA.owner_id[0],
                    OWNER_DATA.columns[1], OWNER_DATA.owner_tax_number[0],
                    OWNER_DATA.columns[2], OWNER_DATA.owner_first_name[0],
                    OWNER_DATA.columns[3], OWNER_DATA.owner_last_name[0],
                    OWNER_DATA.columns[4], OWNER_DATA.owner_company_name[0],
                    OWNER_DATA.columns[5], OWNER_DATA.owner_street[0],
                    OWNER_DATA.columns[6], OWNER_DATA.owner_house_number[0],
                    OWNER_DATA.columns[7], OWNER_DATA.owner_flat_number[0],
                    OWNER_DATA.columns[8], OWNER_DATA.owner_zip_code[0],
                    OWNER_DATA.columns[9], OWNER_DATA.owner_city[0],
                    OWNER_DATA.columns[10], OWNER_DATA.owner_email[0],
                    OWNER_DATA.columns[11], OWNER_DATA.owner_phone_number[0]))

        # splits string on commas
        list_to_change = input(
            "If you want to change some values, enter the names separated by commas or hit Esc. ").split(",")
        print("*" * 30)
        print(list_to_change)
        print("*" * 30)
        # if list_to_change is not empty, change some fields
        if list_to_change:
            for i in list_to_change:
                # gets rid of unnecessary spaces
                if i.replace(" ", "") in OWNER_DATA.columns:
                    OWNER_DATA[i.replace(" ", "")][0] = input(
                        "Enter new value for the field {}: ".format(OWNER_DATA.columns[i]))
        else:
            print("Empty list provided or operation aborted.")


class Contractor:
    CONTRACTOR_DATA = pd.read_csv("contractor.csv")

    '''
    Contractor - class operating on contractors, i.e. customers, suppliers and outsourcing companies
    '''

    def __init__(self, contractor_id=CONTRACTOR_DATA.contractor_id[0],
                 contractor_tax_number=CONTRACTOR_DATA.contractor_tax_number[0],
                 contractor_first_name=CONTRACTOR_DATA.contractor_first_name[0],
                 contractor_last_name=CONTRACTOR_DATA.contractor_last_name[0],
                 contractor_company_name=CONTRACTOR_DATA.contractor_company_name[0],
                 contractor_street=CONTRACTOR_DATA.contractor_street[0],
                 contractor_house_number=CONTRACTOR_DATA.contractor_house_number[0],
                 contractor_flat_number=CONTRACTOR_DATA.contractor_flat_number[0],
                 contractor_zip_code=CONTRACTOR_DATA.contractor_zip_code[0],
                 contractor_city=CONTRACTOR_DATA.contractor_city[0],
                 contractor_email=CONTRACTOR_DATA.contractor_email[0],
                 contractor_phone_number=CONTRACTOR_DATA.contractor_phone_number[0]):

        '''
        init - arguments accepted:
        contractor_id - contractor number in a database,
        contractor_tax_number - contractor tax number (NIP or PESEL),
        contractor_first_name - contractor 1st name,
        contractor_last_name - contractor last name,
        contractor_company_name - contractor company name,
        contractor_street - contractor address (street),
        contractor_house_number - contractor address (house number),
        contractor_flat_number - contractor address (flat number),
        contractor_zip_code - contractor address (zip code),
        contractor_city - contractor address (city),
        contractor_email - contractor email address,
        contractor_phone_number - contractor phone number.
        '''

        self.contractor_id = contractor_id
        self.contractor_tax_number = contractor_tax_number
        self.contractor_first_name = contractor_first_name
        self.contractor_last_name = contractor_last_name
        self.contractor_company_name = contractor_company_name
        self.contractor_street = contractor_street
        self.contractor_house_number = contractor_house_number
        self.contractor_flat_number = contractor_flat_number
        self.contractor_zip_code = contractor_zip_code
        self.contractor_city = contractor_city
        self.contractor_email = contractor_email
        self.contractor_phone_number = contractor_phone_number

    def __str__(self):

        '''
        shows Contractor basic data
        '''

        return """
{} {}
{}
{} {} / {}
{} {}
tax number: {}
""".format(self.contractor_first_name, self.contractor_last_name, self.contractor_company_name,
           self.contractor_street, self.contractor_house_number, self.contractor_flat_number,
           self.contractor_zip_code, self.contractor_city, self.contractor_tax_number
           )

    def add_contractor(self, CONTRACTOR_DATA=CONTRACTOR_DATA):

        """
        :param CONTRACTOR_DATA: class variable
        :return: adds new contractor to the contractors.csv file
        """

        new_contractor = []

        for column in CONTRACTOR_DATA.columns:
            # contractor_id counted and added automatically
            if column == "contractor_id":
                with open('contractor.csv', 'r', newline='\n') as f:
                    first_element_last_line = int(f.readlines()[-1][0])
                    new_contractor.append(first_element_last_line + 1)
            else:
                # all the other parameters added manually
                element_to_add = input("Enter {} or leave blank: ".format(column))
                new_contractor.append(element_to_add)

        with open('contractor.csv', 'a', newline='\n') as f:
            writer = csv.writer(f)
            # write one row
            writer.writerow(new_contractor)


class Invoice(Owner, Contractor):
    '''
    Invoice - class operating on invoices enables to issue new invoices and show existing ones
    '''

    known_kinds = ['invoice', 'correction invoice', 'advance payment invoice', 'final invoice', 'proforma']
    known_tax_rates = [0, 5, 8, 23, "zw", "np", "oo"]

    number_of_invoices = 0
    list_of_invoices = []

    def __init__(self, owner_id, owner_tax_number, owner_first_name,
                 owner_last_name, owner_company_name, owner_street, owner_house_number, owner_flat_number,
                 owner_zip_code, owner_city, owner_email, owner_phone_number,
                 contractor_id, contractor_tax_number,
                 contractor_first_name,
                 contractor_last_name, contractor_company_name,
                 contractor_street, contractor_house_number, contractor_flat_number, contractor_zip_code,
                 contractor_city, contractor_email, contractor_phone_number, invoice_number):
        Owner.__init__(self, owner_id, owner_tax_number, owner_first_name,
                       owner_last_name, owner_company_name, owner_street, owner_house_number, owner_flat_number,
                       owner_zip_code, owner_city, owner_email, owner_phone_number
                       )
        Contractor.__init__(self, contractor_id, contractor_tax_number, contractor_first_name,
                            contractor_last_name, contractor_company_name,
                            contractor_street, contractor_house_number, contractor_flat_number, contractor_zip_code,
                            contractor_city, contractor_email, contractor_phone_number
                            )

        self.invoice_number = str(datetime.date.today().year) + "/" + str(len(self.list_of_invoices) + 1)
        self.issue_date = datetime.date.today()
        self.position = []
        Invoice.number_of_invoices += 1
        Invoice.list_of_invoices.append(self)

    '''
    init - arguments accepted:
    invoice_number - invoice number (unique, assigned automatically)
    contractor_id - contractor number in a database,
    contractor_tax_number - contractor tax number (NIP or PESEL),
    contractor_first_name - contractor 1st name,
    contractor_last_name - contractor last name,
    contractor_company_name - contractor company name,
    contractor_street - contractor address (street),
    contractor_house_number - contractor address (house number),
    contractor_flat_number - contractor address (flat number),
    contractor_zip_code - contractor address (zip code),
    contractor_city - contractor address (city),
    contractor_tax_number - contractor tax number (NIP or PESEL),
    contractor_first_name - contractor 1st name,
    contractor_last_name - contractor last name,
    contractor_company_name - contractor company name,
    contractor_street - contractor address (street),
    contractor_house_number - contractor address (house number),
    contractor_flat_number - contractor address (flat number),
    contractor_zip_code - contractor address (zip code),
    contractor_city - contractor address (city),
    '''

    def add_position(self):
        x = 0
        position_list = []
        while True:
            x += 1
            position = []
            product = input("Type in name of a product/service: ")
            position.append(product)
            unit = input("Type in unit: ")
            position.append(unit)
            try:
                number_of_pieces = float(input("Type in number of pieces: "))
                position.append(number_of_pieces)
            except ValueError:
                position.append(0.0)
            code = input("Type in code for the product/service: ")
            position.append(code)
            try:
                discount = float(input("Type in a discount [0, 100] or leave blank: "))
                if discount < 0 or discount > 100:
                    raise DiscountException("Discount value should be an integer between 0 and 100. Discount 0% will "
                                            "be applied.")
                else:
                    position.append(discount / 100)
            except DiscountException as e:
                print("Discount error. {}".format(e))
                position.append(0.0)
            try:
                net_value = float(input("Type in net value: "))
                position.append(net_value)
            except ValueError:
                position.append(0.0)
            try:
                tax = input("Type in tax rate {}: ".format(self.known_tax_rates))
                # checking if the tax given by a user is on the default tax list
                if tax not in [str(i) for i in self.known_tax_rates] or tax == "":
                    # if the tax given by a user is NOT on the default tax list, a regular rate 23% is applied
                    raise TaxException("Tax type is not on the list: {}. A regular type (23%) will be applied.".format(
                        self.known_tax_rates))
                else:
                    # if the tax is on the list and is a number, will be converted to float and added to the position
                    try:
                        position.append(float(tax))
                    # if the tax is on the list but isn't a number, will be added to the position AS IS
                    except:
                        position.append(tax)
            # if the tax given by a user is NOT on the default tax list, a regular rate 23% is applied
            except TaxException as e:
                print("Tax error. {}".format(e))
                position.append(23 / 100)
            # before the user proceeds, they can see the position
            end = input("""
This is your position:

=========================
Product name:      {}
Unit:              {}
Number of pieces:  {}
Code:              {}
Discount:          {}
Net value:         {}
Tax rate:          {}
=========================

Do you want to add next position ([y]/n) ?""".format(product, unit, number_of_pieces, code, discount, net_value, tax))
            position_list.append(position)
            if end == "y":
                print("{} position(s) added to the invoice".format(len(position_list)))
                continue
            elif end == "n":
                print("{} position(s) added to the invoice".format(len(position_list)))
                break
            else:
                print("Wrong order. If you want to add another position, hit y, otherwise hit n. ")
        print(position_list)  # trzeba coś dodać w stylu wyświetlenie całej faktury i zaakceptowanie

    def calculateSubsumByTaxInInvoice(self):
        pass

    def calculateGlobalSumInInvoice(self):
        pass

    def __str__(self):

        '''
        shows the Invoice
        '''

        return """
====================================
INVOICE NUMBER: {}
issue date: {}
==========
| SELLER |
==========""".format(self.invoice_number, self.issue_date) + Owner.__str__(self) + """
==========
| BUYER  |
==========""" + Contractor.__str__(self)

    def printOut(self):
        pass

    def sendToContractor(self):
        pass

    def sendToAccountant(self):
        pass

    '''
    method for importing incoming invoices, reads from a string divided by semicolons ':'
    '''

    @classmethod
    def ReadFromText(cls, aText):
        aNewInvoice = (aText.split(':'))
        return aNewInvoice

    '''
    method for . . .
    '''

    @staticmethod
    def ConvertEurToPln(EUR):
        return round(EUR * 4.56, 2)

    '''
    method for converting EUR to PLN
    '''

    @staticmethod
    def ConvertPlnToEur(PLN):
        return round(PLN * 0.22, 2)

    '''
    method for converting PLN to EUR
    '''

    @staticmethod
    def ConvertNetToGross(net_value, tax):
        return round(net_value * (1 + tax), 2)

    '''
    method for calculating gross value
    '''


class InvoicePosition:

    def __init__(self, position: str,
                 unit: str,
                 number_of_pieces: float,
                 code: str,
                 discount: float,
                 net_value: float,
                 tax: float):
        self.position = position
        self.unit = unit
        self.number_of_pieces = number_of_pieces
        self.code = code
        self.discount = discount
        self.net_value = net_value
        self.tax = tax


class Database:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def database(self):
        df = pd.DataFrame()
        return df


class InvoiceException(Exception):

    def __init__(self, text):
        super(InvoiceException, self).__init__(text)

    def __str__(self):
        return "{}".format(super().__str__())


class TaxException(InvoiceException):
    pass


class DiscountException(InvoiceException):
    pass


new_owner = Owner()
new_contractor = Contractor(contractor_id=1,
                            contractor_tax_number=987654321,
                            contractor_first_name='Andrzej',
                            contractor_last_name='Nowak',
                            contractor_company_name='Polonex',
                            contractor_street='Boczna',
                            contractor_house_number=1,
                            contractor_flat_number=11,
                            contractor_zip_code='11-111',
                            contractor_city='Warszawa',
                            contractor_email='andrzej@polonex.com',
                            contractor_phone_number=111222333)
new_position = InvoicePosition('sugar', 'kg', 2.5, '234.234.234', 0, 100, .23)
new_invoice = Invoice(owner_id=0,
                      owner_tax_number=1234567890,
                      owner_first_name='Adam',
                      owner_last_name='Nowak',
                      owner_company_name='DrutPol',
                      owner_street='Szkolna',
                      owner_house_number=13,
                      owner_flat_number=None,
                      owner_zip_code='01-111',
                      owner_city='Warszawa',
                      owner_email='smith@drutpol.pl',
                      owner_phone_number=722633544,
                      contractor_id=1,
                      contractor_tax_number=987654321,
                      contractor_first_name='Andrzej',
                      contractor_last_name='Nowak',
                      contractor_company_name='Polonex',
                      contractor_street='Boczna',
                      contractor_house_number=1,
                      contractor_flat_number=11,
                      contractor_zip_code='11-111',
                      contractor_city='Warszawa',
                      contractor_email='andrzej@polonex.com',
                      contractor_phone_number=111222333,
                      invoice_number=1)
# print('*' * 30)
# print(new_owner)
# print('*' * 30)
# print(new_contractor)
# print('*' * 30)
# print(new_invoice)
# # print('*' * 30)
# new_invoice.add_position()
# print(new_invoice.position)
# new_owner = Owner()
# new_owner.change_data()
# new_contractor = Contractor()
Contractor().add_contractor()