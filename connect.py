from zeep import Client
import csv

#Link naar WSDL schema
client = Client('http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl')


#Functie voor VIESCHECK
def wsdl_function(country,btwNo):
    result = client.service.checkVat(country, btwNo)
    print(result['name'])


#wsdl_function(btwCode)

#Een lijst wordt gecreeerd
listofcode  = list()
with open('Importlines.csv', 'r', encoding="ISO-8859-1" ) as f: #delimeter zou er aan toegevoegd kunnen worden
    reader = csv.reader(f)
    for row in reader:
        listofcode.append([row[0],row[1]])

#listofcode.append(['NL','808669291B01'])
#listofcode.append(['NL','823764898B01'])

#Door de lijst wordt geloopt en de functie wordt gecalld
for item in listofcode:
    wsdl_function(item[0],item[1])
