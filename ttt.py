import json
from urllib.request import urlopen
import xmltodict

r = urlopen('https://blog.iservery.com/wp-json/wp/v2/posts')
data = json.load(r)
pole=[]
for radek in data:
  inradek=dict(nadpis=radek['title']['rendered'],xxx=radek['content']['rendered'])
  pole.append(inradek)
#print(pole['0'])
print(inradek)


with open('idk.json', 'r') as f:
    jsonString = f.read()

print('JSON input (sample.json):')
print(jsonString)

xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)

print('\nXML output(output.xml):')
print(xmlString)

with open('output.xml', 'w') as f:
    f.write(xmlString)