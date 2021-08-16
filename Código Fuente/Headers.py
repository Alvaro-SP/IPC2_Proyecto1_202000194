from nodos import *
#todo metodo para insertar un nodo en una lista doblemente enlazada ordenada

class HeaderList():
    def __init__(self, First=None):
        self.First=First

    def setHeader(self, new):
        if self.First==None:
            self.First=new
        elif new.id < self.First.id:
            new.Next=self.First
            self.First.anterior=new
            self.First=new
        else:
            current=self.First
            while current.Next != None:
                if new.id<current.Next.id:
                    new.Next=current.Next
                    current.Next.anterior=current
                    new.anterior=current
                    current.Next=new
                    break
                current=current.Next
            if current.Next==None:
                current.Next=new
                new.anterior=current

    def getHeader(self, id):
        current = self.First
        while current!=None:
            if current.id==id:
                return current
            current=current.Next
        return None