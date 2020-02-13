import argparse
from invogg.generator import InvoggGenerator

DESCRIPTION = 'Generate invoices without sweatin'

def create_parser():
    invoice_gen_parser = argparse.ArgumentParser(prog='invogg',
                                                 description=DESCRIPTION)
    subparsers = invoice_gen_parser.add_subparsers(title='commands', help='command options', dest='command')
    generate_subparser = subparsers.add_parser('generate', help='Generate invoices locally')
    generate_subparser.add_argument('--invoice-template', default=None, help='Specify a yaml file for invoice template variables')
    generate_subparser.add_argument('--invoice-csv', default=None, help='Specify a csv file for invoice')
    return invoice_gen_parser.parse_args()


if __name__ == "__main__":
    args = create_parser()
    if args.command == 'generate':
        generator = InvoggGenerator(args)
        print("Successfully initialized the generator. Generating invoice pdf files....")
        generator.generate_invoice_pdf_files()
        print("Genering invoice pdf files complete.")
