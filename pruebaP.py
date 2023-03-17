from datetime import date

### Hossein Yahyazadeh

### DB
### declaring a dictionary
dataBase = []
today = date.today()

dataBase.append({
        "id":0,
        "estado": "cotizacion",
        "fecha":"2023-03-17",
        "producto":"BMW Serie 1",
        "vendedor": "Javier Gabriel Morales"
    })
dataBase.append({
        "id":1,
        "estado": "proceso",
        "fecha":"2023-03-17",
        "producto":"BMW Serie 2",
        "vendedor": "Armando Villaruel"
    })

dataBase.append({
        "id":2,
        "estado": "cotizacion",
        "fecha":"2023-01-17",
        "producto":"BMW Serie 5",
        "vendedor": "Armando Villaruel"
    })

dataBase.append({
        "id":3,
        "estado": "proceso",
        "fecha":"2023-02-17",
        "producto":"BMW Serie 7",
        "vendedor": "Javier Gabriel Morales"
    })
dataBase.append({
        "id":4,
        "estado": "cotizacion",
        "fecha":"2023-03-17",
        "producto":"Honda",
        "vendedor": "Javier Gabriel Morales"
    })
dataBase.append({
        "id":5,
        "estado": "cotizacion",
        "fecha":"2023-03-15",
        "producto":"Porsche",
        "vendedor": "Armando Villaruel"
    })
dataBase.append({
        "id":6,
        "estado": "proceso",
        "fecha":"17/03/2023",
        "producto":"Mazda S5",
        "vendedor": "Armando Villaruel"
    })

###!SECTION FUNCTIONS

### FUNCTION
def state(state, dataBase, date):

    temporalList = []

    for element in dataBase:
        if element['estado'] == state and element['fecha'] == str(date):
            temporalList.append(element)
        else:
            pass
    return temporalList

### FUNCTION
def orderBy(index, dataBase):
    
    temporalList = []
    temporalNames = []

    for element in dataBase:
        if len(temporalList) == 0:
            temporalList.append([element])
            temporalNames.append(element['vendedor'])
        elif element['vendedor'] in temporalNames:
            index = temporalNames.index(element['vendedor'])
            temporalList[index].append(element)
        else:
            temporalList.append([element])
            temporalNames.append(element['vendedor'])

    return temporalList

###!SECTION
# 0 */12 * * *
# Se requiere crear un cron que ejecute la siguiente acción cada 12 hrs
#   a. Que busque todas las órdenes de venta que se crearon en el día en curso y que se
#       encuentran en cotización
#   b. Agrupar las órdenes de venta por vendedor
#   c. Mandar un correo al vendedor diciendo que tiene tantas ordenes de venta en
#       cotización.

TodasCotizaciones = state('cotizacion', dataBase, today)
print(TodasCotizaciones)

OrderedByName = orderBy('id', dataBase)
print(OrderedByName)