def Check(coordenadas,num_filas,num_col):
    if len(coordenadas) > 2 or len(coordenadas)<2:
        print("Verificar datos! digitar un valor para X y uno para Y")
        pasar=False
    else:
        if not coordenadas[0].isnumeric() or not coordenadas[1].isnumeric():
            print("Solo son valores numeros numericos!")
            pasar=False
        else:
            pasar=True

def check_dimensions(num_filas_usr,num_col_usr,num_fila_matriz,num_col_matriz):
        pasar2=False
        if int(num_filas_usr) > int(num_fila_matriz):
            print("Digite un valor de fila dentro del rango!")
            pasar2 = False
        elif int(num_col_usr) > int(num_col_matriz):
            print("Digite un valor de Columna dentro del rango!")
            pasar2 = False
        else:
            pasar2=True

        return pasar2

def fill_Matriz(matriz,num_filas,num_col):
    for i in range(0,num_filas-1):
        for j in range(0,num_col-1):
            matriz[i][j]=0
    return matriz

def getVecindad(fil,col):
    vecindad=[]
    if fil>0:
        vecindad.append([fil-1,col])
    if fil<3:
        vecindad.append([fil+1,col])
    if col>0:
        vecindad.append([fil,col-1])
    if col<4:
        vecindad.append([fil,col+1])

    return vecindad
