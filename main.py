class Invoice:
    '''
    Class meaning
    '''

    known_kinds = ['invoice', 'correction invoice']

    def __init__(self, kind):
        if kind in self.known_kinds:
            self.kind = kind
        else:
            raise ValueError('This kind of invoice does not exists. Please choose either "invoice" or "correction invoice".')


    def createNewInvoice(self):
        pass


    def printOut(self):
        pass


    def sendToCustomer(self):
        pass


    def sendToAccountant(self):
        pass