import yaml


class InvoiceTemplate():

    def __init__(self, invoice_template_path):
        self.invoice_template_path = invoice_template_path
        self.read_invoice_template()

    def read_invoice_template(self):
        with open(self.invoice_template_path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            if data:
                if 'invoice_template' not in data[0]:
                    print("invoice_template does not exist")
                else:
                    for k, v in data[0].get('invoice_template').items():
                        setattr(self, k, v)

        