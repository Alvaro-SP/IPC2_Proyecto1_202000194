from nodos import *
from Headers import *
from LinkedList import *
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

  
