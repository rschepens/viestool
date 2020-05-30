from zeep import Client

#Link naar WSDL schema
client = Client('http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl')


#Functie voor VIESCHECK
def wsdl_function(btwNo):
    country = btwNo[:2]
    number= btwNo[2:]
    result = client.service.checkVat(country, number)
    print(result['name'])



#wsdl_function(btwCode)

#Een lijst wordt gecreeerd
listofcode  = list()
listofcode.append('NL148250749B01')
listofcode.append('NL823764898B01')

#Door de lijst wordt geloopt en de functie wordt gecalld
for item in listofcode:
    wsdl_function(item)
