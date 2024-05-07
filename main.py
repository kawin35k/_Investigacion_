from clase_persona import persona
import numpy as np
def main():

    #en cada instancia se genera un numero de registro unico
    a,b,c=persona(),persona(),persona()
    a.carga_persona("Dario Marinero","20-35851431-7")
    b.carga_persona("Bautista Poblete","20-4792873-4")
    c.carga_persona("Benjamin Riveros","20-47124715-7")
    print("-----------arreglo desordenado-----------")
    arreglo_personas=np.array([c,b,a])
    for i in range(len(arreglo_personas)):
        print(arreglo_personas[i].mostrar_datos()) 
    print("-----------arreglo ordenado-----------")
    arreglo_personas.sort() # en este caso "sort" ordena los objetos segun su numero de registro
    for j in range(len(arreglo_personas)):
        print(arreglo_personas[j].mostrar_datos()) 

    #se indica el nivel de habilidad en cada area respectivamente
    a.ingresa_habilidades(2,2,4)
    b.ingresa_habilidades(5,5,5)
    c.ingresa_habilidades(9,5,3)
    print("----sobrecarga SUMA ----")
    acum_persona=persona() #acumulador de personas
    for k in range(len(arreglo_personas)):
        acum_persona+=arreglo_personas[k] # en accion la sobrecarga del operador "+"
    print(acum_persona.dame_habilidades())
    print("----sobrecarga DIVICION ----")
    promedio_persona=acum_persona/len(arreglo_personas) # en accion la sobrecarga del operador "/"
    print(promedio_persona.dame_habilidades())

if __name__=='__main__':
    main()