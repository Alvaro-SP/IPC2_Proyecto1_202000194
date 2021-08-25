class Node:
    def __init__(self, row, column, value):
        self.row=row
        self.column=column
        self.value=value 
        self.derecha=None
        self.izquierda=None
        self.arriba=None
        self.abajo=None

class nodoHeaders:
    def __init__(self, id):
        self.id=id
        self.Next=None
        self.anterior=None
        self.accessNode=None
