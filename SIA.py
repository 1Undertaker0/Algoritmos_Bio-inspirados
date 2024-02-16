import random
import string

class SIA :    
    
    caracteres_permitidos = list(string.ascii_letters + ' ')
    
    def __init__(self) :
        self.max_iteraciones = 1000
        self.cantidad_anticuerpos = 20 #Poblacion inicial de anticuerpos
        self.antigeno = list('A Pedrito le gusta mucho la vecina') #Cadena que tratara de replicar
        self.porcentaje_mutacion = 0.1 #Tasa de mutación, del 0 al 1
        self.poblacion = []
        self.nueva_poblacion_clonada = []
        self.id_anticuerpo = 1
        
    def ordenar_poblacion(self) :
        self.poblacion.sort(key=lambda poblacion: poblacion[0], reverse=True)
    
    def ordenar_poblacion_clonada(self) :
        self.nueva_poblacion_clonada.sort(key=lambda poblacion: poblacion[0], reverse=True)
        
    def crear_anticuerpo(self) :
        nuevo_anticuerpo = []
        for i in range(len(self.antigeno)) :
            nuevo_anticuerpo.append(random.choice(self.caracteres_permitidos))
        return nuevo_anticuerpo
        
    
    def crear_poblacion_inicial(self) :
        for i in range(self.cantidad_anticuerpos) :
            individuo = [self.id_anticuerpo, self.crear_anticuerpo(), []]
            self.id_anticuerpo += 1
            self.poblacion.append(individuo)
            
    def evaluacion_antigeno(self) :
        posiciones_antigeno = []
        for parte in self.antigeno :
            posiciones_antigeno.append(self.caracteres_permitidos.index(parte))
        return posiciones_antigeno
            
    def funcion_objetivo(self, anticuerpo) :
        puntaje = []
        cantidad = len(anticuerpo)
        calificion = 0
        antigeno = self.evaluacion_antigeno()
        for i in range(cantidad) :
            pos_ac = self.caracteres_permitidos.index(anticuerpo[i]) #Posicion de cada parte del anticuerpo en el diccionario
            pos_ag = antigeno[i]  #Posicion de cada parte del antigeno en el diccionario
            if pos_ac < pos_ag : calificion += ((pos_ag - pos_ac) * 100/len(self.caracteres_permitidos))* -1
            elif pos_ac > pos_ag : calificion += (pos_ac - pos_ag) * 100/len(self.caracteres_permitidos)
            puntaje.append(calificion)
        
        return puntaje, sum(puntaje)
            
    def evalucion_poblacion(self) :
        for anticuerpo in self.poblacion :
            anticuerpo[2], anticuerpo[0] = self.funcion_objetivo(anticuerpo[1])
        self.ordenar_poblacion()
    
    def clonacion(self, punto_max) :
        i = 0
        for anticuerpo in self.poblacion :
            self.nueva_poblacion_clonada.append(anticuerpo)
            i += 1
            if i == punto_max : break
    
    def configuracion_mutacion(self, calif, anti) :
        nuevo_caracter = ''
        if calif < 0 :
            nuevo_caracter = self.caracteres_permitidos[random.randint(self.caracteres_permitidos.index(anti), len(self.caracteres_permitidos) - 1)]
        elif calif > 0 :
            nuevo_caracter = self.caracteres_permitidos[random.randint(0, self.caracteres_permitidos.index(anti))]
        else:
            nuevo_caracter = anti
        return nuevo_caracter
    
    def mutacion(self, clonado, calif) :
        for i in range(len(clonado)) :
            p = random.uniform(0, 1)
            if p < self.porcentaje_mutacion :
                clonado[i] = self.configuracion_mutacion(calif[i], clonado[i])
        return clonado
            
    def seleccion(self) :
        porcentaje_aceptacion = (random.randint(40, 60) * self.cantidad_anticuerpos // 100) - 1
        self.clonacion(porcentaje_aceptacion)
        for anti_clonado in self.nueva_poblacion_clonada :
            anti_clonado[1] = self.mutacion(anti_clonado[1], anti_clonado[2])
            anti_clonado[2], anti_clonado[0] = self.funcion_objetivo(anti_clonado[1])
        self.ordenar_poblacion_clonada()
            
        
    def reemplazo(self) :
        limite_anterior = len(self.nueva_poblacion_clonada) - 1
        aux = 0
        for i in range(len(self.poblacion) - limite_anterior, len(self.poblacion) - 1) :
            self.poblacion[i] = self.nueva_poblacion_clonada[aux]
            aux += 1
            if i == len(self.poblacion) - 1 :
                self.poblacion.append(self.nueva_poblacion_clonada[aux])
                break
        self.ordenar_poblacion()
        self.nueva_poblacion_clonada = []
        
    def sistema_inmune(self) :
        i = 1
        self.crear_poblacion_inicial()
        self.evalucion_poblacion()
    
        while i <= self.max_iteraciones :
            self.seleccion()
            self.reemplazo()
        
            if i % 5 == 0:
                print("Iteracion: " + str(i + 1))
                print("Mejor resultado: " + str(self.poblacion[0][1]))
            i += 1
                
if __name__ == '__main__' :
    a = SIA()
    a.sistema_inmune()
    