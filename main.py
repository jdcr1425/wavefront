import methods

num_filas=4
num_col=5

pasar=False
while(pasar==False):

    p_inicio=input("Digite la coordenada de inicio. Escriba los valores de x y y separados por coma : \n")
    coor_inicio=p_inicio.split(",")
    methods.Check(coor_inicio,int(num_filas),int(num_col))
    if methods.check_dimensions(coor_inicio[0],coor_inicio[1],num_filas,num_col):
        pasar=True

pasar=False
while(pasar==False):
    p_fin=input("Digite la coordenada de fin. Escriba los valores de x y y separados por coma : \n")
    coor_fin=p_fin.split(",")
    methods.Check(coor_fin,int(num_filas),int(num_col))
    if methods.check_dimensions(coor_fin[0], coor_fin[1], num_filas, num_col):
        if coor_inicio == coor_fin:
            print("Error! No puede asignar la misma coordenada de inicio")
            pasar=False
        else:
            pasar=True


"""matriz = []
for i in range(num_filas):
    matriz.append([0] * num_col)
"""


#1)etiquetar todos los estados con obstaculos con el valor "-1"
matriz=[[0, 0, 0,  0, 0],
        [0, 0,-1, -1, 0],
        [0, 0, 0, -1, 0],
        [0, 0, 0, -1, 0]]

print(matriz)



