import numpy as np
from clase_persona import persona
from crea_equipo import Equipo

equipo1=Equipo(3)


per3=persona()
per3.carga_persona("C","3")
#print(per.mostrar_datos())
per3.ingresa_habilidad(2,5)
per4=persona()
per4.carga_persona("D","4")
per4.ingresa_habilidad(2,8)
per5=persona()
per5.carga_persona("E","5")
per5.ingresa_habilidad(2,10)
per1=persona()
per1.carga_persona("A","1")
#print(per.mostrar_datos())
per1.ingresa_habilidad(2,4)
#print(per1.dame_habilidades().max()) FUNCIONA
per2=persona()
per2.carga_persona("B","2")
per2.ingresa_habilidad(2,3)
#def __add__(otro):
 #   return np.array(np.concatenate([otro]))

a=np.array([1,2,3])
b=np.array([3,2,1])
c=a+b
persona_suma=per1+per2
print("cero print")
print(per5.dame_habilidades())
print("primer print de la sobrecarga suma")
print(persona_suma.dame_habilidades())
print(persona_suma.mostrar_datos())
div=persona_suma/2
print("primer print de la sobrecarga divicion")
print(div.dame_habilidades())
print(div.mostrar_datos())

listaDePersonas=[per1,per2,per3,per4,per5]
a=[]
#for i in listaDePersonas:   #este for es el de la linea 23 del comulo crea_equipo
 #   a.append(i.dame_area(2))#concatena(agrega) elementos al arreglo
print("por entrar sobrecarga_orden")
sobrecarga_orden=per1<per3
print(sobrecarga_orden)
equipo1.crea_automatico(listaDePersonas,2)
#casteo=np.array(equipo1).sort QUIZA DESPUES
#print(equipo1.dame_equipo())
print("segundo print")
print(per1.mostrar_datos())
print("tercer print")
print(listaDePersonas[2].mostrar_datos())

#a=2
#perslita=[per1,per2]
lista=[1,5000,4,3,2,7,8,9,9,5]
arr=np.array(listaDePersonas)
arr.sort()
#brr=np.empty(a,dtype=int)
#b=np.array(perslita)
#b=np.concatenate((arr,[100]),axis=0)   de esta forma se puede concatenar arreglos
print("ultimo print")
print(arr[0].mostrar_datos())
#print(listaArea.max())