#!Persona 1
Personaje1 = (input('ingrese el nombre del personaje'))
Altura1 = (input('ingrese el altura del personaje')) 
Peso1 = int(input('ingrese el peso del personaje')) 
Planeta1 = (input('ingrese el planta del personaje')) 
Peliculas1 = int(input('ingrese el peliiculasd del personaje')) 
 
#!Persona 2 
Personaje2 = (input('ingrese el nombre del personaje'))
Altura2 = (input('ingrese el altura del personaje')) 
Peso2 = int(input('ingrese el peso del personaje')) 
Planeta2 = (input('ingrese el planta del personaje')) 
Peliculas2 = int(input('ingrese el peliiculasd del personaje'))  


Pers1 = [Personaje1, Altura1, Peso1, Planeta1, Peliculas1]
Pers2 = [Personaje2, Altura2, Peso2, Planeta2, Peliculas2]

#! 1-b: 

if (Pers1[2] > Pers2[2]):
    print(Pers1[0], 'es mas pesado')
elif (Pers1[2]) == Pers2[2]:
    print('pesan lo mismo')
else:
     (Pers2[0], 'es mas pesado')

#! 1-c:

if (Pers1[4] > Pers2[4]):
    print(Pers1[0], 'participo en mas pelis')
elif (Pers1[4]) == Pers2[4]:
    print('participaron en las mismas pelis')
else:
    (Pers2[0], 'participo en mas pelis') 

#!1-a:

if (Pers2[1] > Pers1[1]):
    print(Pers2[0], 'es mas alto')
elif(Pers1[1]) == Pers2[1]:
    print('miden lo mismo')    
else:
    print(Pers1[0], 'es mas bajo')

#! 1-d:

if(Personaje1.capitalize() == "Yoda" or Personaje1.capitalize() == "Chewbacca" or Personaje2.capitalize()== "Yoda" or Personaje2.capitalize() == "Chewbacca"):
    print("Uno de los personajes se llama Yoda o Chew")
else:
    print("Ninguno de los personajes se llama Yoda o Chew")