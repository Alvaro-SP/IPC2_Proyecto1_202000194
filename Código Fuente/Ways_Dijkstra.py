import math

class Vertice:

	# se añaden los vertices que va a contener cada uno de los nodos que le mando
	def __init__(self, i):

		#!INICIO DE LOS VERTICES Y SUS ATRIBUTOS
		self.id = i
		self.vecinos = []
		self.visitado = False
		self.padre = None
		self.costo = float('inf')

	def agregarVecino(self, v, p):
		 
		if v not in self.vecinos:
			self.vecinos.append([v, p])

class Grafica:
	 
	def __init__(self):
		#* vertices de la grafica
		self.vertices = {}

	def agregarVertice(self, id):
		"""se añaden vertices recibiendo ."""
		if id not in self.vertices:
			self.vertices[id] = Vertice(id)

	def agregarArista(self, nodo1, nodo2, valuegas):		
		if nodo1 in self.vertices and nodo2 in self.vertices:
			self.vertices[nodo1].agregarVecino(nodo2, valuegas)
			self.vertices[nodo2].agregarVecino(nodo1, valuegas)

	def imprimirGrafica(self):
		
		for vert in self.vertices:
			print("El costo del vértice "+str(self.vertices[vert].id)+" es "+ str(self.vertices[vert].costo)+" llegando desde "+str(self.vertices[vert].padre))
			
	
	def camino(self, start, end):
		
		wayofmymatriz = []
		actual = end
		while actual != None:
			wayofmymatriz.insert(0, actual)
			actual = self.vertices[actual].padre
		return [wayofmymatriz, self.vertices[end].costo]
		# while erow!=None :#and ecolumn!=None:
                #     current=erow.accessNode
                #     #colcurrent=ecolumn.accessNode
                    
                #     while current!=None : #colcurrent!=None:
                        
                #         #matriz_adya[eme][ene]=current.value
                #         if current.value!=None:
                #             print(current.value)
                #         # print("posicion: (", current.row, " , ", current.column, ") --> gasolina", current.value)
                #         # print("posicion derecha: (", current.derecha.row, " , ", current.derecha.column,") --> gasolina derecha: ", current.derecha.value)
                #         # print("posicion abajo: (", current.abajo.row, " , ", current.abajo.column,") --> gasolina abajo: ", colcurrent.abajo.value)
                        
                #         #elif current.row == current.column+1:
                #             #matriz_adya[eme][ene]=current.izquierda.value+current.derecha.value+current.abajo.value
                                    
                #         current=current.derecha                
                #     erow=erow.Next
            

	def minimo(self, l):
		
		if len(l) > 0:
			m = self.vertices[l[0]].costo
			v = l[0]
			for e in l:
				if m > self.vertices[e].costo:
					m = self.vertices[e].costo
					v = e
			return v
		return None

	def dijkstra(self, start):
		# ? PROCEDIMIENTO DE DIJKSTRA Y EXPLICACION DE COMO FUNCIONA:
		# ? El algoritmo de Dijkstra, también llamado algoritmo de caminos 
		# mínimos, es un algoritmo para la determinación del camino más corto, 
		# dado un vértice origen, hacia el resto de los vértices en un grafo que 
		# tiene pesos en cada arista.

		# fuente la wikipedia
		# while erow!=None :#and ecolumn!=None:
                #     current=erow.accessNode
                #     #colcurrent=ecolumn.accessNode
                    
                #     while current!=None : #colcurrent!=None:
                        
                #         #matriz_adya[eme][ene]=current.value
                #         if current.value!=None:
                #             print(current.value)
                #         # print("posicion: (", current.row, " , ", current.column, ") --> gasolina", current.value)
                #         # print("posicion derecha: (", current.derecha.row, " , ", current.derecha.column,") --> gasolina derecha: ", current.derecha.value)
                #         # print("posicion abajo: (", current.abajo.row, " , ", current.abajo.column,") --> gasolina abajo: ", colcurrent.abajo.value)
                        
                #         #elif current.row == current.column+1:
                #             #matriz_adya[eme][ene]=current.izquierda.value+current.derecha.value+current.abajo.value
                                    
                #         current=current.derecha                
                #     erow=erow.Next
            
		if start in self.vertices:
			# 1 y 2
			self.vertices[start].costo = 0
			actual = start
			noVisitados = []
			
			for v in self.vertices:
				if v != start:
					self.vertices[v].costo = float('inf')
				self.vertices[v].padre = None
				noVisitados.append(v)

			while len(noVisitados) > 0:
			
				for vec in self.vertices[actual].vecinos:
					if self.vertices[vec[0]].visitado == False:				
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
							self.vertices[vec[0]].padre = actual

				
				self.vertices[actual].visitado = True
				noVisitados.remove(actual)

				
				actual = self.minimo(noVisitados)
		else:
			return False