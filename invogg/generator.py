import os
import sys
import requests
import json

from invogg.invoice_template import InvoiceTemplate
from invogg.invoice import Invoices

DIR_NAME = os.path.dirname(os.path.abspath(__file__))

class InvoggGenerator():

    TARGET_URL = "https://invoice-generator.com"


    def __init__(self, args=None):
        self.args = args
        self.invoice_template = self.create_invoice_template(self.args.invoice_template)
        self.invoices = self.create_invoices(self.args.invoice_csv)

    def create_invoice_template(self, invoice_template_path):
        if invoice_template_path:
            invoice_template_path = os.path.abspath(invoice_template_path)
        else:
            invoice_template_path = os.path.join(DIR_NAME, 'default_invoice_template.yml')
        
        invoice_template = InvoiceTemplate(invoice_template_path=invoice_template_path)
        return invoice_template
    
    def create_invoices(self, invoice_path):
        if invoice_path:
            invoice_path = os.path.abspath(invoice_path)
        else:
            print("Invoice path is invalid")
            sys.exit(1)
        
        invoices = Invoices(invoice_path)
        return invoices
    
    def generate_invoice_pdf_files(self):

        for num, invoice in enumerate(self.invoices.invoice_list):
            payload = invoice.identity
            headers = {'Content-type': 'application/json'}
            r = requests.post(InvoggGenerator.TARGET_URL, data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print("[{}]--------Successfully generated an invoice for {}".format(num+1, invoice.name))
                with open(os.path.abspath(os.path.join(DIR_NAME, os.pardir, 'generated_pdfs', invoice.name + '.pdf')), 'wb+') as fd:
                    fd.write(r.content)

        


        