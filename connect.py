from zeep import Client
import csv
from datetime import datetime
now = datetime.now()

#Link naar WSDL schema
client = Client('http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl')

outputlist = list()
#Functie voor VIESCHECK
def wsdl_function(refno,country,btwNo):
    i = 1
    while True:
        now = datetime.now()
        try:
            result = client.service.checkVat(country, btwNo)
            address1 = result['address']
            address = address1.replace("\n", "|")
            name = result['name']
            valid = result['valid']
            break
        except:
            i = i + 1
            address = "-1"
            name = "-1"
            valid = "-1"

        if (i > 5):
            break

        outputlist.append([refno, valid])



#wsdl_function(btwCode)

#Een lijst wordt gecreeerd
listofcode  = list()
with open('Importlines.csv', 'r', encoding="ISO-8859-1" ) as f: #delimeter zou er aan toegevoegd kunnen worden
    reader = csv.reader(f)
    for row in reader:
        listofcode.append([row[0],row[1],row[2]])

#listofcode.append(['NL','808669291B01'])
#listofcode.append(['NL','823764898B01'])
listlength = len(listofcode)
j = 0
#Door de lijst wordt geloopt en de functie wordt gecalld
for item in listofcode:
    wsdl_function(item[0],item[1],item[2])
    j += 1
    print(j/listlength)
