import datetime


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

invoice01 = Invoice('2021/02/01', 'Concert', 1000)
invoice02 = Invoice('2021/02/02', 'Scores', 597)
invoice02.show_info()