red = input("Indica la red")
redSeparada = red.split(".")
mascara = input("Indica la mascara")
print(redSeparada)

# Libreria de Mascaras y host utiles
mascara_Hosts = {
    30:2,
    29:6,
    28:14,
    27:30,
    26:62,
    25:126,
    24:254,
    23:510,
    22:1022,
    21:2046,
    20:4094,
    19:8190,
    18:16382,
    17:32766,
    16:65534,
    15:131070,
    14:262142,
    13:524286,
    12:1048574,
    11:2097150,
    10:4194302,
    9:8388606,
    8:16777214
}

#Creamos una Lista que absorna el tamaño de las diferentes subredes
HostSubredes = []
x = "N"
while x != "Y":
    #nombreSubred = input("Nombre de subred")
    hostSubred = int(input("Host de la subred"))
    HostSubredes.append(hostSubred)
    x = input("¿Has introducidos todas las subredes? Y/N : ")

#subredes = sorted(subredes.items())
#print(subredes)
#Ordenamos las subredes de tamaño mayor a menor
HostSubredes.sort(reverse=True)
print(HostSubredes)

"""
for i in mascara_Hosts:
    print(mascara_Hosts[i])
"""
#Creamos el diccionario que asociara el tamaño de la subred con la mascara
Subred_mascara = {}
iterante=1

# Estos loops anidados asocian la subredes con la mascara apropiada
for x in HostSubredes:

    encontrado = False
    i = 30
    while i >= 8 and not encontrado:
        if mascara_Hosts[i] >= x:
            Subred_mascara["red"+str(iterante)]=i
            encontrado = True
            iterante+=1
        i-=1

print(Subred_mascara)

diccionarioSalida = {}
if int(mascara)%8 == 0:
    print("Es multiplo de 8")
    if int(mascara) == 24:
        print("Es 24")
        redSeparada[3] = 0
        itinerante = 0
        for i in Subred_mascara:
            print("entre")
            RedLista = redSeparada[0:3]
            subred = redSeparada[3]
            broadcast = int(subred) + mascara_Hosts[Subred_mascara[i]]+1
            diccionarioSalida["Subred"+str(itinerante)] ={"red": ".".join(RedLista) + "." + str(subred), "mascara": Subred_mascara[i] ,"broadcast": ".".join(RedLista) + "." + str(broadcast), "Rango":".".join(RedLista) + "." + str(int(subred)+1) + "-" + str(broadcast - 1) }
            redSeparada[3] = broadcast + 1
            itinerante += 1
    
    if mascara == 16:
        redSeparada[3] = 0
        redSeparada[2] = 0
    if mascara == 8:
        redSeparada[3] = 0
        redSeparada[2] = 0
        redSeparada[1] = 0
print(diccionarioSalida)