from clase_persona import persona
import numpy as np

lucho=persona()
mateo=persona()
kevin=persona()
kevin.carga_persona("dario","20358514317")

lucho.carga_persona("lucho","123456")
mateo.carga_persona("mateo","654987")
print(lucho<mateo)



lista=[mateo,lucho,kevin]
arr=np.array(lista)
hola="hola"
mundo=" mundo"
hola_mundo=hola+mundo
print(hola_mundo)