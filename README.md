# invogg

## Background
https://invoice-generator.com/ is a great website for generating a free invoice with a simple UI. 

However, it is hard to manage multiple invoices. 

What if an excel spreadsheet (.csv file) can be used to generate multiple invoices easily? Well, here is your solution.

## Get Started

### Prerequisites:
1. Python 3.6 installed
2. Pip3
3. Git
4. Sane mind

### How to run:
1. Run ```git clone https://github.com/arctan5x/invogg.git```
2. Run ```cd invogg```
3. Run ```pip install -r requirements.txt```
4. Run ```python -m invogg generate --invoice-template path/to/template.yml --invoice-csv path/to/csv```
* i.e. ```python -m invogg generate --invoice-template sample_invoice_template.yml --invoice-csv sample_invoices.csv```

## Notes

- Used APIs from https://github.com/Invoiced/invoice-generator-api.

- All yaml attributes for default invoice template should be in the template path. (HAVE NOT IMPLEMENTED USING AN ACTUAL TEMPLATE).

- Take a look at sample_invoices.csv for an example. Do NOT modify column headers or their sequence. Only add more item columns if you need more.

- If you want to edit addressess or notes with multiline, make sure that there is a newline char (in raw) or use Excel to edit the multiline.

