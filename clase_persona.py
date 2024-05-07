import numpy as np

class persona:
    __generaNroregistro=1000
    __NroRegistro=str
    __cuil=str
    __Nyp=str
    __area=3
    __planilla=None
    __ocupado=False
    def __init__(self):
        self.__planilla=np.zeros(self.__area,dtype=int)
        self.__NroRegistro=str(self.__generaNroregistro)
        self.__cuil="nulo"
        self.__Nyp="nulo"
        persona.incrementaNareg(1)
    @classmethod
    def incrementaNªreg(cls,x):
        cls.__generaNroregistro+=x
    def carga_persona(self,xNyP,xcuil):
        self.__Nyp=xNyP
        self.__cuil=xcuil
    def actualiza_habilidad(self,xarea,xnivel):
        self.__planilla[xarea]=xnivel
    def ingresa_habilidades(self,a1,a2,a3):
        self.__planilla[0]=a1
        self.__planilla[1]=a2
        self.__planilla[2]=a3
    def dame_habilidades(self):
        return self.__planilla 
    def dame_area(self,xarea):
        return self.__planilla[xarea]
    def mostrar_datos(self):
        dic={"Nº registro":self.__NroRegistro,"Nombre":self.__Nyp,"cuil":self.__cuil,"ocupado":self.__ocupado}
        return dic
    def actualizar_ocupado(self,estado):
        self.__ocupado=estado
    def dame_ocupado(self):
        return self.__ocupado
#SOBRECARGA DE OPERADORES 
    def __add__(self,otros):
        a=self.__planilla
        b=otros.__planilla
        nueva_persona=persona()
        nueva_persona.__planilla=a+b
        nueva_persona.incrementaNareg(-1)#esto es para que no incremente sin sentido el atributo de clase
        nueva_persona.__NroRegistro="0"
        return nueva_persona
    def __truediv__(self, divide_por):
        if divide_por == 0: # Verificar si el denominador del otro objeto no es cero
            raise ValueError("El denominador del divisor no puede ser cero.")
        a=self.__planilla
        b=divide_por
        nueva_persona=persona()
        nueva_persona.__planilla=np.round(a/b).astype(int)
        return nueva_persona
    def __lt__(self, otro): # aqui indico que al ordenar estas intancias lo hagan por el numero de registo    
        return self.__NroRegistro < otro.__NroRegistro

      
    
    