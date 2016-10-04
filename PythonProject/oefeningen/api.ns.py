import requests

import xmltodict

auth_details = ('sam.morssinkhof@student.hu.nl', 'jlQ_NwJcf9nvQeeE98MOnyZLO_WuCiwlcekTrUkBRRg1M1hw5b7w2A')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

response = requests.get(api_url, auth=auth_details)

with open('vertrektijden.xml', 'w') as myXMLFile:
    myXMLFile.write(response.text)


