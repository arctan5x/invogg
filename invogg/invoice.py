import csv

class Invoice():

    ATTRIBUTES = set(["logo", "from", "from_address", "to", "to_address", "number", "purchase_order", "due_date", "discounts", "tax", "shipping", "amount_paid", "notes", "terms"])

    def __init__(self, headers, data):
        self.items = {}
        self.data = data
        self.headers = headers
        if len(self.headers) != len(self.data):
            print("Number of headers and data don't match up. Check your invoice csv")
        self.identity = {}
        self.name = "N/A"
        self.initialize_identity()

        
    def initialize_identity(self):
        self.identity['items'] = []
        for i in range(len(self.headers)):
            if self.data[i]:
                if self.headers[i] in Invoice.ATTRIBUTES:
                    if self.headers[i] == "to":
                        self.name = self.data[i]
                    if self.headers[i] == "from_address":
                        self.identity["from"] += '\n' + self.data[i]
                    elif self.headers[i] == "to_address":
                        self.identity["to"] += '\n' + self.data[i]
                    else:
                        self.identity[self.headers[i]] = self.data[i]
                elif 'item' in self.headers[i]:
                    if 'name' in self.headers[i]:
                        self.identity['items'].append({"name": self.data[i]})
                    elif 'quantity' in self.headers[i]:
                        self.identity['items'][-1]['quantity'] = float(self.data[i])
                    elif 'unit_cost' in self.headers[i]:
                        self.identity['items'][-1]['unit_cost'] = float(self.data[i])
                    elif 'description' in self.headers[i]:
                        self.identity['items'][-1]['description'] = self.data[i]


class Invoices():

    def __init__(self, invoice_path):
        self.invoice_list = []
        self.invoice_path = invoice_path
        self.read_invoice_csv()
        

    def read_invoice_csv(self):
        with open(self.invoice_path) as csvfile:
            csvreader = csv.reader(csvfile)
            headers = None
            for row in csvreader:
                if not headers:
                    headers = row
                else:
                    self.invoice_list.append(Invoice(headers, row))

                    

