import networkx as nx
import random
import matplotlib.pyplot as plt

# Crear un grafo dirigido
class Hormiguero:
    def __init__(self) -> None:
        self.grafo = nx.DiGraph()
        self.iteraciones = 5
        self.comida = 100000000000
        self.mejor_distancia = 0
        self.mejor_solucion = []
        self.poblacion_hormiga = []
        self.nodo_hormiguero = 'A'
        self.nodo_comida = 'T'
        self.cantidad_fermona_global = 0.01
        self.cantidad_hormiga = 10
        self.cantidad_fermonaXH = 2
        self.tasa_evaporacion = 0.5
        self.influencia_feromona = 2
        self.influencia_peso = 1
        
    def generadorHormigas(self,cantidad) -> None:
        for i in range(cantidad) :
            self.poblacion_hormiga.append([i, [self.nodo_hormiguero], self.nodo_hormiguero])
        #print(poblacion_hormiga)
        

    def crear_campo(self) :        
        # Agregar nodos
        #campo = ["A", "B", "C", "D", "F", "H", "J", "K", "L"]
        #campo = ["A", "B", "C", "D", "E", "F", "G"]
        campo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
        
        self.grafo.add_nodes_from(campo)
        
        """("A", "B", {'weight' : 1.5, 'fermona' : self.cantidad_fermona_global}),
                ("A", "E", {'weight' : 1, 'fermona' : self.cantidad_fermona_global}),
                ('B', 'C', {'weight' : 3.7, 'fermona' : self.cantidad_fermona_global}),
                ("C", "D", {'weight' : 1.2, 'fermona' : self.cantidad_fermona_global}),
                ("C", "F", {'weight' : 0.7, 'fermona' : self.cantidad_fermona_global}),
                ("C", "B", {'weight' : 3.7, 'fermona' : self.cantidad_fermona_global}),
                ("D", "E", {'weight' : 2.6, 'fermona' : self.cantidad_fermona_global}),
                ("E", "F", {'weight' : 1.6, 'fermona' : self.cantidad_fermona_global}),
                ("E", "C", {'weight' : 0.4, 'fermona' : self.cantidad_fermona_global}),
                ("E", "A", {'weight' : 1.8, 'fermona' : self.cantidad_fermona_global}),
                ("F", "G", {'weight' : 0.9, 'fermona' : self.cantidad_fermona_global}),
                ("F", "C", {'weight' : 0.4, 'fermona' : self.cantidad_fermona_global}),
                ("F", "B", {'weight' : 0.7, 'fermona' : self.cantidad_fermona_global})"""
                
                
        """('A', 'B', {'weight': 0.52, 'fermona': self.cantidad_fermona_global}),
        ('A', 'C', {'weight': 0.75, 'fermona': self.cantidad_fermona_global}),
        ('B', 'D', {'weight': 0.83, 'fermona': self.cantidad_fermona_global}),
        ('B', 'E', {'weight': 1.12, 'fermona': self.cantidad_fermona_global}),
        ('C', 'F', {'weight': 1.21, 'fermona': self.cantidad_fermona_global}),
        ('C', 'G', {'weight': 1.33, 'fermona': self.cantidad_fermona_global}),
        ('D', 'H', {'weight': 1.42, 'fermona': self.cantidad_fermona_global}),
        ('D', 'I', {'weight': 1.63, 'fermona': self.cantidad_fermona_global}),
        ('E', 'J', {'weight': 1.79, 'fermona': self.cantidad_fermona_global}),
        ('E', 'K', {'weight': 1.81, 'fermona': self.cantidad_fermona_global}),
        ('F', 'L', {'weight': 2.06, 'fermona': self.cantidad_fermona_global}),
        ('F', 'M', {'weight': 2.19, 'fermona': self.cantidad_fermona_global}),
        ('G', 'N', {'weight': 2.38, 'fermona': self.cantidad_fermona_global}),
        ('G', 'O', {'weight': 2.47, 'fermona': self.cantidad_fermona_global}),
        ('H', 'P', {'weight': 2.64, 'fermona': self.cantidad_fermona_global}),
        ('H', 'Q', {'weight': 2.78, 'fermona': self.cantidad_fermona_global}),
        ('I', 'R', {'weight': 2.82, 'fermona': self.cantidad_fermona_global}),
        ('I', 'S', {'weight': 2.91, 'fermona': self.cantidad_fermona_global}),
        ('J', 'Q', {'weight': 3.17, 'fermona': self.cantidad_fermona_global}),
        ('K', 'T', {'weight': 3.28, 'fermona': self.cantidad_fermona_global}),
        ('L', 'C', {'weight': 3.33, 'fermona': self.cantidad_fermona_global}),
        ('M', 'B', {'weight': 3.51, 'fermona': self.cantidad_fermona_global}),
        ('N', 'L', {'weight': 3.64, 'fermona': self.cantidad_fermona_global}),
        ('O', 'P', {'weight': 3.73, 'fermona': self.cantidad_fermona_global}),
        ('P', 'G', {'weight': 3.93, 'fermona': self.cantidad_fermona_global}),
        ('Q', 'T', {'weight': 4.08, 'fermona': self.cantidad_fermona_global}),
        ('R', 'S', {'weight': 4.28, 'fermona': self.cantidad_fermona_global}),
        ('S', 'T', {'weight': 4.42, 'fermona': self.cantidad_fermona_global})"""
                                
        """("A","B",         {'weight': 0.5  , 'fermona' : self.cantidad_fermona_global}), 
                ("A","FILIPINAS", {'weight': 0.9  , 'fermona' : self.cantidad_fermona_global}),
                ("B","C",         {'weight': 0.18 , 'fermona' : self.cantidad_fermona_global}),
                ("C","D",         {'weight': 0.67 , 'fermona' : self.cantidad_fermona_global}),
                ("D","F",         {'weight': 0.4  , 'fermona' : self.cantidad_fermona_global}),
                ("A","F",         {'weight': 1 , 'fermona' : self.cantidad_fermona_global}),
                ("F","H",         {'weight': 0.60 , 'fermona' : self.cantidad_fermona_global}),
                ("H","J",         {'weight': 0.023, 'fermona' : self.cantidad_fermona_global}),
                ("H","K",         {'weight': 1.02 , 'fermona' : self.cantidad_fermona_global}),
                ("K","L",         {'weight': 0.9, 'fermona' : self.cantidad_fermona_global}),
                ("D","J",         {'weight': 0.09 , 'fermona' : self.cantidad_fermona_global})"""

        # Agregar arcos
        self.grafo.add_edges_from(
            [
                ("A","B",         {'weight': 0.5  , 'fermona' : self.cantidad_fermona_global}), 
                ("A","FILIPINAS", {'weight': 0.9  , 'fermona' : self.cantidad_fermona_global}),
                ("B","C",         {'weight': 0.18 , 'fermona' : self.cantidad_fermona_global}),
                ("C","D",         {'weight': 0.67 , 'fermona' : self.cantidad_fermona_global}),
                ("D","F",         {'weight': 0.4  , 'fermona' : self.cantidad_fermona_global}),
                ("A","F",         {'weight': 1 , 'fermona' : self.cantidad_fermona_global}),
                ("F","H",         {'weight': 0.60 , 'fermona' : self.cantidad_fermona_global}),
                ("H","J",         {'weight': 0.023, 'fermona' : self.cantidad_fermona_global}),
                ("H","K",         {'weight': 1.02 , 'fermona' : self.cantidad_fermona_global}),
                ("K","L",         {'weight': 0.9, 'fermona' : self.cantidad_fermona_global}),
                ("D","J",         {'weight': 0.09 , 'fermona' : self.cantidad_fermona_global})
            ]
            #'A', 'C', 'G', 'O', 'T'
        )
        #Dibujar el grafo
        pos = nx.circular_layout(self.grafo)  # Diseño circular para el ejemplo
        nx.draw(self.grafo, pos, with_labels=True, arrows=True)
        labels = {(i, j): d["weight"] for i, j, d in self.grafo.edges(data=True)}
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.show()
        
    def get_vecinos(self,nodo):
        a = []
        for node in self.grafo.nodes():
            bol = self.grafo.has_edge(nodo,node)
            if bol:
                a.append(node)
        return a
    
    def get_vecinos_excepto(self, nodo, excluyente) :
        resultado = []
        for node in self.grafo.nodes() :
            if self.grafo.has_edge(nodo, node) :
                if node != excluyente :
                    resultado.append(node)
        return resultado

    def nodo_ant(self, vecinos, anterior) :
        if anterior in vecinos :
            if len(vecinos) != 0:
                vecinos.remove(anterior)
                return vecinos
            else :
               return []
        return vecinos
    
    def value_next_node(self, nodo_vecino, ant) :
        sum_all_street = 0
        p = []
        for nodo in nodo_vecino :
            sum_all_street += (self.grafo.edges[ant, nodo]['fermona']**self.influencia_feromona * (1/self.grafo.edges[ant, nodo]['weight'])**self.influencia_peso)
        for opcion in nodo_vecino :
            p.append(((self.grafo.edges[ant, opcion]['fermona']**self.influencia_feromona * (1/self.grafo.edges[ant, nodo]['weight'])**self.influencia_peso) / (sum_all_street)))
        return p
    
    def nivel_fermona(self, fermona, arco) :
        return ((1 - self.tasa_evaporacion) * fermona + (self.cantidad_fermonaXH/self.grafo.edges[arco]['weight']))
    
    def elegir_arco(self, nodo_vecino, ant) :
        porcentajes = []
        pase = random.randint(1, 100)
        suma_probabily = 0
        valor_x_nodo = self.value_next_node(nodo_vecino, ant)
        print(nodo_vecino, valor_x_nodo)
        for nodo in valor_x_nodo :
            porcentajes.append(nodo*100/sum(valor_x_nodo))
        for i in range(len(porcentajes)) :
            suma_probabily += porcentajes[i]
            if not pase > suma_probabily :
                return i
        return 0

    def retornar_hormiga(self, ant) :
        camino_h = ant[1]
        camino_h.remove(ant[2])
        nodo_sin_camino = ant[2]
        ant[1] = camino_h
        ant[2] = camino_h[len(camino_h) - 1]
        return ant, nodo_sin_camino
            
    def mover_hormiga(self) :
        for hormiga_actual in self.poblacion_hormiga:
            vecinos= self.get_vecinos(hormiga_actual[2])
            if len(hormiga_actual[1]) >= 2: 
                vecinos = self.nodo_ant(vecinos, (hormiga_actual[1])[len(hormiga_actual[1]) - 2])
            if len(vecinos) == 0 : 
                hormiga_actual, excepcion = self.retornar_hormiga(hormiga_actual)
                vecinos = self.get_vecinos_excepto(hormiga_actual[2], excepcion)
            index = self.elegir_arco(vecinos, hormiga_actual[2])
            next_node = vecinos[index]
            hormiga_actual[1].append(next_node)
            #print("Hormiga " + str(hormiga_actual[0]) + ": " + str(hormiga_actual[1]))
            self.depuracion_fermona(hormiga_actual[2], next_node)
            hormiga_actual[2] = next_node
            hormiga_actual[1] = self.comprobar_comida(hormiga_actual[1])
            if hormiga_actual[1][len(hormiga_actual[1]) - 1] != hormiga_actual[2] :
                hormiga_actual[2] = 'A'
    
    def comprobar_comida(self, hormiga) :
        if hormiga[len(hormiga) - 1] == self.nodo_comida :
            self.comida -= 1
            hormiga = self.actualizar_global(hormiga)
            for n in range(len(hormiga) - 1, 0, -1) :
                self.grafo.edges[hormiga[n-1], hormiga[n]]['fermona'] = self.nivel_fermona(self.grafo.edges[hormiga[n-1], hormiga[n]]['fermona'], [hormiga[n - 1], hormiga[n]])
            #print(self.grafo.edges(data=True))
            if self.mejor_distancia != 0 :
                distancia = self.actualizar_distancia(hormiga)
                if distancia < self.mejor_distancia :
                    self.mejor_distancia = distancia
                    self.mejor_solucion = hormiga
                
            hormiga = ['A']
            return hormiga
        else :
            #print(self.poblacion_hormiga)
            return hormiga
            
            
    def actualizar_global(self, opcion) :
        for i in range(len(opcion)) :
            if not opcion.count(opcion[i]) == 0 :
                repetido = [a for a, x in enumerate(opcion) if x == i]
                for e in repetido :
                    opcion.remove(e)
        distancia = self.actualizar_distancia(opcion)
        if self.mejor_solucion != [] and self.mejor_distancia != 0 and opcion != [] and self.mejor_distancia > distancia:
            self.mejor_solucion = opcion
            self.mejor_distancia = distancia
        elif self.mejor_solucion == [] and self.mejor_distancia == 0:
            self.mejor_solucion = opcion
            self.mejor_distancia = distancia
        return opcion
                
    def actualizar_distancia(self, camino) :
        r = 0
        for nodo in range(len(camino) - 1) : 
            r += self.grafo.edges[camino[nodo], camino[nodo + 1]]['weight']
        return r
    
    def coloniaHormigas(self):
        self.generadorHormigas(self.cantidad_hormiga)
        self.crear_campo()
        for i in range(self.iteraciones) :
            self.mover_hormiga()
            if i % 1 == 0:
                print("Iteracion: " + str(i))
                print("Mejor solucion: " + str(self.mejor_solucion))
                print("Mejor distancia: " + str(self.mejor_distancia))
                print('Comida restante: ' + str(self.comida))
                print('------------------------------------------------------\n')
        self.imprime_caminos_hormigas()
        
    def depuracion_fermona(self, nodo_actual, nodo_siguiente) :
        fermona_actual = self.grafo.edges[nodo_actual, nodo_siguiente]['fermona']
        if fermona_actual != self.cantidad_fermona_global :
            self.grafo.edges[nodo_actual, nodo_siguiente]['fermona'] = (1 - self.influencia_feromona) * fermona_actual
    
    def imprime_caminos_hormigas(self) :
        poblacion = self.poblacion_hormiga
        for i in range(len(poblacion)) :
            camino = poblacion[i]
            print("Hormiga" , i + 1, ": " + str((camino[1])))
            
if __name__ == '__main__' :
    amlo = Hormiguero()
    amlo.coloniaHormigas()
    