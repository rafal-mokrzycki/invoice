'''class PersonOrCompany(object):

    def __init__(self, id):
        self.id = id'''


class Owner:

    def __init__(self, owner_id):
        print('>>class Owner - init - starting')
        self.owner_id = owner_id
        #super().__init__(owner_id)
        print('>>class Owner - init - finishing')


class Contractor:

    def __init__(self, contractor_id):
        print('>>class Contractor - init - starting')
        self.contractor_id = contractor_id
        #super().__init__(contractor_id)
        print('>>class Contractor - init - finishing')


class Invoice(Owner, Contractor):

    def __init__(self, owner_id, contractor_id, invoice_id):
        print('>>class Invoice - init - starting')
        self.invoice_id = invoice_id
        Owner.__init__(self, owner_id)
        Contractor.__init__(self, contractor_id)
        print('>>class Invoice - init - finishing')



invoice = Invoice(1,2,3)
print(vars(invoice))
print('*'*30)
print(invoice.invoice_id)
print(invoice.owner_id)
print(invoice.contractor_id)