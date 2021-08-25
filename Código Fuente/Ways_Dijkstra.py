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

	def agregarArista(self, a, b, p):
		
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)

	def imprimirGrafica(self):
		
		for vert in self.vertices:
			print("El costo del vértice "+str(self.vertices[vert].id)+" es "+ str(self.vertices[vert].costo)+" llegando desde "+str(self.vertices[vert].padre))
			
	
	def camino(self, a, b):
		
		wayofmymatriz = []
		actual = b
		while actual != None:
			wayofmymatriz.insert(0, actual)
			actual = self.vertices[actual].padre
		return [wayofmymatriz, self.vertices[b].costo]

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

	def dijkstra(self, a):
		# ? PROCEDIMIENTO DE DIJKSTRA Y EXPLICACION DE COMO FUNCIONA:
		# ? El algoritmo de Dijkstra, también llamado algoritmo de caminos 
		# mínimos, es un algoritmo para la determinación del camino más corto, 
		# dado un vértice origen, hacia el resto de los vértices en un grafo que 
		# tiene pesos en cada arista.

		# fuente la wikipedia
		if a in self.vertices:
			# 1 y 2
			self.vertices[a].costo = 0
			actual = a
			noVisitados = []
			
			for v in self.vertices:
				if v != a:
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
