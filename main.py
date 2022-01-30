import datetime

class Owner:

    '''
    Owner of the program and person/company issuing invoices. Must be unique.
    '''

    def __init__(self,
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
                 owner_phone_number=722633544)

        '''
        init - arguments accepted:
        id - object number in a database,
        tax_number - object tax number (NIP or PESEL),
        first_name - object 1st name,
        last_name - object last name,
        company_name - object company name,
        street - object address (street),
        house_number - object address (house number),
        flat_number - object address (flat number),
        zip_code - object address (zip code),
        city - object address (city),
        email - object email address,
        phone_number - object phone number.
        '''

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

class Contractor:

    number_of_contractors = 0
    list_of_contractors = []
    '''
    Contractor - class operating on contractors, i.e. customers, suppliers and outsourcing companies
    '''

    def __init__(self, id, tax_number, first_name, last_name, company_name, street, house_number,
                 flat_number, zip_code, city, email, phone_number):

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
        self.id = id
        self.tax_number = tax_number
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.street = street
        self.house_number = house_number
        self.flat_number = flat_number
        self.zip_code = zip_code
        self.city = city
        self.email = email
        self.phone_number = phone_number
        Contractor.number_of_contractors += 1
        Contractor.list_of_contractors.append(self)

    def show_info(self, kind):
        print("Contractor ID:\t{}".format(self.id))
        print("Tax number:\t\t{}".format(self.tax_number))
        print("First name:\t\t{}".format(self.first_name))
        print("Last name:\t\t{}".format(self.last_name))
        if kind == 'full':
            print("Address:\t\t{} {}/{}, {} {}".format(self.street, self.house_number, self.flat_number,
                                                       self.zip_code, self.city))
            print("E-mail:\t\t\t{}".format(self.email))
            print("Phone number:\t{}".format(self.phone_number))
        print('-' * 20)

    def add_contractor(self):

        pass

class Invoice(Owner, Contractor):

    ##################################################################################################################
    #                                                                                                                #
    #                                USTAWIĆ DZIEDZICZENIE Z WIELU KLAS!!!                                           #
    #                                                                                                                #
    ##################################################################################################################
    '''
    Class meaning
    '''

    known_kinds = ['invoice', 'correction invoice', 'advance payment invoice', 'final invoice', 'proforma']
    known_tax_rates = [0.0, 0.5, 0.8, 0.23, "zw", "np", "oo"]

    number_of_invoices = 0
    list_of_invoices = []

    '''
    Zgodnie z przepisami ustawy o podatku od towarów i usług art. 106e ust. 1 faktura powinna zawierać co najmniej:

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

    def __init__(self, invoice_number, contractor_id, contractor_first_name, contractor_last_name, contractor_street, contractor_house_number,
                 contractor_flat_number, contractor_zip_code, contractor_city, contractor_tax_number, delivery_date,
                 kind = "invoice", issue_date=str(datetime.datetime.today()).split()[0],
                 issuer_first_name='Adam', issuer_last_name='Smith',
                 issuer_street='Main Street', issuer_house_number='11', issuer_flat_number='22', issuer_zip_code='00543',
                 issuer_city='London', issuer_tax_number='123456789'):

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
        delivery_date - delivery date
        kind - invoice kind, to be chosen from: ['invoice', 'correction invoice', 'advance payment invoice', 'final invoice', 'proforma'],
        issue_date -issue date
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

        '''
        issuer data
        '''

        self.issuer_first_name = issuer_first_name
        self.issuer_last_name = issuer_last_name
        self.issuer_street = issuer_street
        self.issuer_house_number = issuer_house_number
        self.issuer_flat_number = issuer_flat_number
        self.issuer_zip_code = issuer_zip_code
        self.issuer_city = issuer_city
        self.issuer_tax_number = issuer_tax_number
        '''
        contractor data
        '''
        self.contractor_id = contractor_id
        self.contractor_first_name = contractor_first_name
        self.contractor_last_name = contractor_last_name
        self.contractor_street = contractor_street
        self.contractor_house_number = contractor_house_number
        self.contractor_flat_number = contractor_flat_number
        self.contractor_zip_code = contractor_zip_code
        self.contractor_city = contractor_city
        self.contractor_tax_number = contractor_tax_number
        '''
        invoice data
        '''
        self.delivery_date = delivery_date
        self.issue_date = issue_date
        self.invoice_number = invoice_number
        self.positions = []
        if kind in self.known_kinds:
            self.kind = kind
        else:
            raise ValueError('This kind of invoice does not exists. Please choose either \
                             "invoice", "correction invoice", "advance payment invoice", "final invoice" or "proforma".')
        self.list_of_invoices.append(self)

    def issue_invoice(self):
        pass

    def add_invoice_position(self):
        pass

    def calculate_subsum_by_tax_rate_in_invoice(self):
        pass

    def calculate_global_sum_in_invoice(self):
        pass

    def printOut(self):
        pass

    def sendToContractor(self):
        pass

    def sendToAccountant(self):
        pass

    def show_info(self):
        print(self.kind.upper())
        print("Number:\t{}".format(self.invoice_number))
        print("Date:\t{}".format(self.issue_date))
        print("Position:\t{}".format(self.position))
        print("Price net: {}".format(self.price_net))
        print("Tax: {}".format(self.tax))
        print("Price gros: {}".format(self.price_net * (1 + self.tax)))
        print('-' * 20)

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

help(Contractor)
invoice = Invoice()
invoice.list_of_invoices()