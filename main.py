# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}
# list(map(print,audi.values()))


def showObjectKeys(list):
    for item in list:
      print (item)

showObjectKeys(audi.values())