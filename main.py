import datetime
import re


class Owner:
    '''
    class Owner defines the owner of the programm and issuer of all invoices
    '''

    def __init__(self,
                 login='login',
                 password='password',
                 owner_id=0,
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
                 owner_phone_number=722633544):
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

    def show_owner(self):

        '''
        shows Owner basic data
        '''

        print("=" * 10, " OWNER ", "=" * 10)
        print("""ID:\t\t\t\t{}
Tax No.:\t\t{}
First Name:\t\t{}
Last Name:\t\t{}
Company Name:\t{}""".format(self.owner_id, self.owner_tax_number, self.owner_first_name, self.owner_last_name,
                            self.owner_company_name))
        print("=" * 30)

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


class Contractor:
    number_of_contractors = 0
    list_of_contractors = []

    '''
    Contractor - class operating on contractors, i.e. customers, suppliers and outsourcing companies
    '''

    def __init__(self, contractor_id, contractor_tax_number, contractor_first_name, contractor_last_name,
                 contractor_company_name,
                 contractor_street, contractor_house_number, contractor_flat_number, contractor_zip_code,
                 contractor_city,
                 contractor_email, contractor_phone_number):
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
        Contractor.number_of_contractors += 1
        Contractor.list_of_contractors.append(self)

    def show_contractor(self):
        print("=" * 8, " CONTRACTOR ", "=" * 8)
        print("""ID:\t\t\t\t{}
Tax No.:\t\t{}
First Name:\t\t{}
Last Name:\t\t{}
Company Name:\t{}""".format(self.contractor_id, self.contractor_tax_number, self.contractor_first_name,
                            self.contractor_last_name,
                            self.contractor_company_name))
        print("=" * 30)

    def add_contractor(self):
        pass


class Invoice(Owner, Contractor):
    '''
    Invoice - class operating on invoices enables to issue new invoices and show existing ones
    '''

    known_kinds = ['invoice', 'correction invoice', 'advance payment invoice', 'final invoice', 'proforma']
    known_tax_rates = [0.0, 0.5, 0.8, 0.23, "zw", "np", "oo"]

    invoices = []

    '''
    Zgodnie z przepisami   ustawy o podatku od towarów i usług art. 106e ust. 1 faktura powinna zawierać co najmniej:

    datę wystawienia,
    kolejny numer nadany w ramach jednej lub więcej serii, który w sposób jednoznaczny ją identyfikuje,
    imiona i nazwiska lub nazwę podatnika i nabywcy towarów lub usług oraz ich adresy,
    numer, za pomocą którego podatnik jest zidentyfikowany na potrzeby podatku,
    numer, za pomocą którego nabywca towarów lub usług jest zidentyfikowany na potrzeby podatku lub podatku od wartości dodanej, 
    pod którym otrzymał on towary lub usługi,
    datę dokonania lub zakończenia dostawy towarów albo wykonania usługi bądź datę otrzymania zapłaty, 
    jeżeli nastąpiła ona przed sprzedażą, o ile taka data jest określona i różni się od daty wystawienia faktury,
    nazwę (rodzaj) towaru lub usługi,
    miarę i ilość (liczbę) dostarczonych towarów lub zakres wykonanych usług,
    cenę jednostkową towaru lub usługi bez kwoty podatku (cenę jednostkową netto),
    kwoty wszelkich upustów lub obniżek cen, w tym w formie rabatu z tytułu wcześniejszej zapłaty, 
    o ile nie zostały one uwzględnione w cenie jednostkowej netto,
    wartość dostarczonych towarów lub wykonanych usług, objętych transakcją bez kwoty podatku (wartość sprzedaży netto),
    stawkę podatku,
    sumę wartości sprzedaży netto z podziałem na sprzedaż objętą poszczególnymi stawkami podatku i sprzedaż zwolnioną od podatku,
    kwotę podatku od sumy wartości sprzedaży netto z podziałem na kwoty dotyczące poszczególnych stawek podatku,
    kwotę należności ogółem.

    Zobacz więcej: https://poradnikprzedsiebiorcy.pl/-elementy-faktury-vat
    '''

    def __init__(self, invoice_number, contractor_id, contractor_tax_number, contractor_first_name,
                 contractor_last_name, contractor_company_name,
                 contractor_street, contractor_house_number, contractor_flat_number, contractor_zip_code,
                 contractor_city, contractor_email, contractor_phone_number,
                 issue_date=datetime.date.today()):
        Owner.__init__(self, owner_id, owner_tax_number, owner_first_name,
                       owner_last_name, owner_company_name, owner_street, owner_house_number, owner_flat_number,
                       owner_zip_code, owner_city, owner_email, owner_phone_number)
        Contractor.__init__(self, contractor_id, contractor_tax_number, contractor_first_name,
                            contractor_last_name, contractor_company_name,
                            contractor_street, contractor_house_number, contractor_flat_number, contractor_zip_code,
                            contractor_city, contractor_email, contractor_phone_number)

        self.invoice_number = invoice_number
        self.issue_date = issue_date

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

    def calculateSubsumByTaxInInvoice(self):
        pass

    def calculateGlobalSumInInvoice(self):
        pass

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
    method for converting EUR to PLN
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
invoice01 = Invoice(

for i in Invoice.invoices:
    i.show_info()

contractor01 = Contractor(contractor_id=26541, contractor_tax_number=5242563258, contractor_first_name='Adam',
                          contractor_last_name='Nowak', contractor_street='Hoża', contractor_house_number=23,
                          contractor_flat_number=17, contractor_zip_code='00-174', contractor_city='Warszawa',
                          contractor_email='adam.nowak@gmail.com', contractor_phone_number=654789321)
contractor01.show_info('basic')
print('*' * 30)
contractor01.show_info('full')
'''

# help(Contractor)
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

'''new_owner.show_owner()
new_contractor.show_contractor()
#new_owner.set_new_password()
a = Invoice.ConvertEurToPln(10)
print(a)'''

print(vars(new_owner))
print(new_owner.owner_city)
print(new_owner._Owner__password)
print('=' * 30)
new_owner.password = ''
print('=' * 30)
print(new_owner._Owner__password)

'''print('='*30)
a,b=new_owner._Owner__get_login_and_password()
print(a,b)
print('='*30)
c=new_owner.set_new_password()
print(c)'''
