#se declaran diccionarios = objetos

clienteUno = {
    'id':5,
    'nombre':'edif1',
    'consumo':200
}

clienteDos = {
    'id':6,
    'nombre':'edif2',
    'consumo':300
}

clienteTres = {
    'id':7,
    'nombre':'edif3',
    'consumo':400
}
#SE DECLARA UNA LISTA = ARREGLO

clienteAsociado=[
    clienteUno,
    clienteDos,
    clienteTres

]

#COMO UTILIZAR LA LISTA?
#MI OBJETIVO SERA OBTENER LA INFORMACION DE LA LISTA 
#RECKRRER UNA LINDA O ARREGLO
#print(clienteAsociado)
 
#aplicando llaves cuadradas podemos buscar entre los bloques algo en especifico
'''for i in range(3):
    print(clienteAsociado[i]['nombre'])'''

#Foreach espezialidado en recorrer arreglos (Lista)

'''for cliente in clienteAsociado:
    print(cliente  ['id'], '=>', cliente ['consumo'], 'KWH')'''

print(f'{cliente['id']} =>{cliente['consumo']} KWH')