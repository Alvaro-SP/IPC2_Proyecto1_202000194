import abc
import time
from os import strerror
from nodos import *
from Headers import *
from LinkedList import *
from Ways_Dijkstra import *

#from main_proyecto1 import *#

positions_ordered_x=LinkedList()
positions_ordered_y=LinkedList()
fuels_ordered =LinkedList()

class matriz():
    def __init__(self):
        self.eRows=HeaderList()
        self.eColumns=HeaderList()

    def insert(self, row, column, value):
        new=Node(row, column, value)
        # inserción encabezado por filas
        erow=self.eRows.getHeader(row)
        if erow==None:
            erow=nodoHeaders(row)
            erow.accessNode=new
            self.eRows.setHeader(erow)
            
        else:
            if new.column<erow.accessNode.column:
                new.derecha=erow.accessNode
                erow.accessNode.izquierda=new
                erow.accessNode=new
            else:
                current=erow.accessNode
                while current.derecha!=None:
                    if new.column<current.derecha.column:
                        new.derecha=current.derecha
                        current.derecha.izquierda=new
                        new.izquierda=current.derecha
                        current.derecha=new
                        break
                    current=current.derecha
                if current.derecha==None:
                    current.derecha=new
                    new.izquierda=current
        
        ecolumn=self.eColumns.getHeader(column)
        if ecolumn==None:
            ecolumn=nodoHeaders(column)
            ecolumn.accessNode=new
            self.eColumns.setHeader(ecolumn)
            
        else:
            if new.row<ecolumn.accessNode.row:
                new.abajo=ecolumn.accessNode
                ecolumn.accessNode.arriba=new
                ecolumn.accessNode=new
                
            else:
                current=ecolumn.accessNode
                while current.abajo!=None:
                    if new.row<current.abajo.row:
                        new.abajo=current.abajo
                        current.abajo.arriba=new
                        new.arriba=current
                        current.abajo=new
                        break
                    current=current.abajo
                if current.abajo ==None:
                    current.abajo=new
                    new.arriba=current
        
    
    
    def recorrerows(self):
        global positions_ordered_x
        global positions_ordered_y
        global fuels_ordered

        erow=self.eRows.First        
        while erow!=None:
            current=erow.accessNode
            #print("\n Fila ,  columna  ,  valor de gasolina\n")
            while current!=None:
                # print(str(current.column)+"     "+current.value)
                print("(",str(current.row),",",current.column,")  --> ",current.value)
                positions_ordered_x.My_Append(int(current.row))
                positions_ordered_y.My_Append(int(current.column))
                fuels_ordered.My_Append(int(current.value))                
                current=current.derecha
            erow=erow.Next        

    def recorrecolumns(self,m,n):
        ecolumn=self.eColumns.First
        print("\n-----------RECORRIDO COLUMNAS--------------")
        while ecolumn!=None:
            current=ecolumn.accessNode
            print("\n Columna: "+str(current.column))
            print("Fila valor")
            while current!=None:
                print(str(current.row)+"     "+current.value)
                current=current.abajo
            ecolumn=ecolumn.Next
        print("-----------FIN RECORRIDO COLUMNAS--------------")  
    #* en esta funcion se mandan los valores de las gasolinas y de las posicones para Obtener los caminos.
    def optimize_ways(self,xo, yo, xf,  yf, m, n):


        g = Grafica()

        matriz_size=int(m)*int(n) 

        erow=self.eRows.First

        start=str(xo)+","+str(yo)

        end=str(xf)+","+str(yf)
        print(start)
        print(end)

        #VERTICES
        # ac=0
        # for em in range(int(m)):
        #     for en in range(int(n)):
        #         vertices.append(str(em)+","+str(en))
        #         print(vertices[ac])
        #         g.agregarVertice(str(vertices[ac]))   #! se agregan los vertices
        #         ac+=1

        #Relación de NODOS
        print("---------------------------------------------")
        ultimogas=0
        # erow=self.eRows.First
        # cont=0
        # for r in range(int(m)*int(n)):
        #     current=erow.accessNode
        #     if cont<=int(n):
                
        #         print(current.value)

        #         cont+=1

        #         current=current.derecha
        #     else:
        #         cont=0
        #         erow=erow.Next 
        print("comienza el proceso de agregar los nodos enlazados usando la lista de listas, (agrego vertices y aristas simulando grafos)")
       
        
        while erow!=None:
            current=erow.accessNode
            
            while current!=None:

                verti=str(current.row)+","+str(current.column)
                g.agregarVertice(str(verti))

                #print("     (",str(current.row),",",current.column,")  --> ",current.value)
                
                try:
                    if current.derecha.row!=None:
                        a=str(current.row)+","+str(current.column)
                        b=str(current.derecha.row)+","+str(current.derecha.column)
                        c=int(current.derecha.value)
                        g.agregarArista(a,b,c)
                        print("(",a,",",b,")  =>  ",c)
                       # print("se agrego vertice a la derecha")
                except Exception as e:
                    #print (e)
                    pass
                
                try:
                    if current.izquierda.row!=None:
                        a=str(current.row)+","+str(current.column)
                        b=str(current.izquierda.row)+","+str(current.izquierda.column)
                        c=int(current.izquierda.value)
                        g.agregarArista(a,b,c)
                        print("(",a,",",b,")  =>  ",c)
                       # print("se agrego vertice a la izquierda")
                except Exception as e:
                    #print (e)
                    pass
                
                try:
                    if current.arriba.row!=None:
                        a=str(current.row)+","+str(current.column)
                        b=str(current.arriba.row)+","+str(current.arriba.column)
                        c=int(current.arriba.value)
                        g.agregarArista(a,b,c)
                        print("(",a,",",b,")  =>  ",c)
                        #print("se agrego vertice arriba")
                except Exception as e:
                    #print (e)
                    pass
                
                try:
                    if current.abajo.row!=None:
                        a=str(current.row)+","+str(current.column)
                        b=str(current.abajo.row)+","+str(current.abajo.column)
                        c=int(current.abajo.value)
                        g.agregarArista(a,b,c)
                        print("(",a,",",b,")  =>  ",c)
                        #print("se agrego vertice abajo")
                except Exception as e:
                    #print (e)
                    pass

                # try:
                #     a=str(current.row)+","+str(current.column)                    
                    
                #     if a==end:
                #         ultimogas=current.value
                #         print("ultimo gas")
                # except Exception as e:
                #     #print (e)
                #     pass

                current=current.derecha

            erow=erow.Next  
        g.imprimirGrafica()
        print(end)
        print("\n\n     Calculando la mejor ruta:  ... ***")
        time.sleep(1)
        print("         Calculando la cantidad de combustible:  ... ***")
        time.sleep(1)

        print("\n       LISTO !:  ")

        print("\n       POSICIÓN INICIAL (",start,")")
        print("     POSICIÓN FINAL (",end,")\n")

        print("\n\n             La mejor Ruta es:  ... ***")

        g.dijkstra(start) #? aqui va el eje x y Y de donde inicia el recorrido


        wayslist,fuelobtain=g.camino(start, end)

        print(wayslist) #? aqui va el eje x y Y de donde inicia y termina el recorrido

        print("\n\n             El valor del combustible es:  ... ***")

        try:

            print(fuelobtain)
            if fuelobtain!="inf":
                fuelobtain=int(fuelobtain)+int(ultimogas)

            print(fuelobtain , "unidades de gasolina")
            self.imprimir_matriz(int(m), int(n), wayslist)
        except:
            print("No se puede concluir el recorrido, ya sea que dos o mas caminos son iguales o")
            print("el valor sobrepasa la cantidad de combustible necesaria del robot R2e2")
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
            
                
                # #!ME QUEDE EN CREAR UNA MATRIZ PARA GUARDAR LOS DATOS DE MI MATRIZ DE ADYACENCIA.
                # while erow!=None:
                #     current=erow.accesNode
                #     while current!=None:     

                #         fila=current.row
                #         column=current.column
                #         gasolina=current.value
                #         if current.row==0:
                #             current.row=current.value+current.derecha.value
                        
                        
                        
                #         current=current.derecha

    def imprimir_matriz(self, m, n, wayslist):
        cadena = ""

        for c in range(1,n+1):
            cadena += "\t" + str(c)

        cadena += "\n " + ("\t-" * int(n))

        for f in range(1,m+1):
            cadena += "\n" + str(f) + " |"


            for c in range(1,n+1):

                cooractual=str(f)+","+str(c)

               

                if cooractual in wayslist:
                    cadena += "\t" + "1"
                else:
                    cadena += "\t" + "0"

                    # if f == c and (m[f][c] is None or m[f][c] == 0):
                    #     cadena += "\t" + "1"
                    # else:
                    #     if m[f][c] is None or math.isinf(m[f][c]):
                    #         cadena += "\t" + "X"
                    #     else:
                    #         cadena += "\t" + str(m[f][c])

        cadena += "\n"
        print(cadena)

    #!  PRUEBAS DE FLOYD - WARSHALL
matriz_size = 6
INF = "INF"

# Algorithm 
def floyd(G):
    distances = list(map(lambda p: list(map(lambda q: q, p)), G))

    # Adding vertices individually
    for r in range(matriz_size):
        for p in range(matriz_size):
            for q in range(matriz_size):
                distances[p][q] = min(distances[p][q], distances[p][r] + distances[r][q])
                
    sol(distances)

# Printing the output
def sol(dist):
    for p in range(matriz_size):
        for q in range(matriz_size):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")



