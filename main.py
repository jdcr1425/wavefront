import methods

num_filas=4
num_col=5

matriz=[[0, 0, 0,  0, 0],
        [0, 0,-1, -1, 0],
        [0, 0, 0, -1, 0],
        [0, 0, 0, -1, 0]]

pasar=False
while(pasar==False):

    p_inicio=input("Digite la coordenada de inicio. Escriba los valores de x y y separados por coma : \n")
    coor_inicio=p_inicio.split(",")
    methods.Check(coor_inicio,int(num_filas),int(num_col))
    if methods.check_dimensions(coor_inicio[0],coor_inicio[1],num_filas,num_col):
        if matriz[int(coor_inicio[0])][int(coor_inicio[1])] == -1:
            print("Esa cooredenada pertenece a un obstaculo")
        else:
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
        elif matriz[int(coor_fin[0])][int(coor_fin[1])] == -1:
            print("Esa cooredenada pertenece a un obstaculo")
        else:
            pasar=True


"""matriz = []
for i in range(num_filas):
    matriz.append([0] * num_col)
"""


#1)etiquetar todos los estados con obstaculos con el valor "-1"


matriz[int(coor_fin[0])][int(coor_fin[1])]=1
acum=2
pos_actual = [int(coor_fin[0]), int(coor_fin[1])]
parar=False
vec_actual=[]




vecindad = methods.getVecindad(pos_actual[0], pos_actual[1])
for i in range(0, len(vecindad)):
    vec_actual = vecindad[i]
    if matriz[vec_actual[0]][vec_actual[1]] == 0:
                 matriz[vec_actual[0]][vec_actual[1]] = acum
pos_actual = [vec_actual[0], vec_actual[1]]



for i in matriz:
    print(i)













