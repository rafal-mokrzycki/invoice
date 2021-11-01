import datetime


class Customer:
    '''
    Class meaning
    '''

    def __init__(self, id, tax_no, first_name, last_name, street, house_no, flat_no, zip_code, city, email, phone_no):
        self.id = id
        self.tax_no = tax_no
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.house_no = house_no
        self.flat_no = flat_no
        self.zip_code = zip_code
        self.city = city
        self.email = email
        self.phone_no = phone_no

    def show_info(self, kind):
        print("Customer ID:\t{}".format(self.id))
        print("Tax number:\t\t{}".format(self.tax_no))
        print("First name:\t\t{}".format(self.first_name))
        print("Last name:\t\t{}".format(self.last_name))
        if kind == 'full':
            print("Address:\t\t{} {}/{}, {} {}".format(self.street, self.house_no, self.flat_no,
                                                self.zip_code, self.city))
            print("E-mail:\t\t\t{}".format(self.email))
            print("Phone number:\t{}".format(self.phone_no))
        print('-' * 20)


class Invoice:
    '''
    Class meaning
    '''

    known_kinds = ['invoice', 'correction invoice']

    invoices = []

    def __init__(self, number, position, priceNet,
                 tax=0.23, date=str(datetime.datetime.today()).split()[0], kind='invoice'):
        self.date = date
        self.number = number
        self.position = position
        self.priceNet = priceNet
        self.tax = tax
        if kind in self.known_kinds:
            self.kind = kind
        else:
            raise ValueError('This kind of invoice does not exists. Please choose either '
                             '"invoice" or "correction invoice".')
        self.invoices.append(self)



    def calculateSumInInvoice(self):
        pass

    def printOut(self):
        pass

    def sendToCustomer(self):
        pass

    def sendToAccountant(self):
        pass

    def show_info(self):
        print(self.kind.upper())
        print("Number:\t{}".format(self.number))
        print("Date:\t{}".format(self.date))
        print("Position:\t{}".format(self.position))
        print("Price net: {}".format(self.priceNet))
        print("Tax: {}".format(self.tax))
        print("Price gros: {}".format(self.priceNet * (1 + self.tax)))
        print('-' * 20)

invoice01 = Invoice('2021/02/01', 'Concert', 1000, kind='correction invoice')
invoice02 = Invoice('2021/02/02', 'Scores', 597)

for i in Invoice.invoices:
    i.show_info()

customer01 = Customer(id = 26541, tax_no = 5242563258, first_name='Adam', last_name = 'Nowak', street = 'Hoża', house_no = 23,
                      flat_no = 17, zip_code = '00-174', city = 'Warszawa',
                      email='adam.nowak@gmail.com', phone_no=654789321)
customer01.show_info('basic')
print('*'*30)
customer01.show_info('full')
