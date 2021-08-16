from thenodo import *
class LinkedList():
    def __init__(self): # * initialize the informatiion of the linkedlist
        self.First=None 
        self.size=0     # * long of the list

    def My_Append(self, value): # * here we add a node in the list
        Mynodo = thenodo(value)
        if self.size == 0:   # ? if the list length is empty change the place o the first
            self.First = Mynodo
        else:
            current = self.First  # * first node of the list
            while current.Next != None:
                current= current.Next
            current.Next = Mynodo
        self.size += 1
        return Mynodo

    def My_remove(self, value):
        if self.size == 0:
            return print("tamaño 0")
        else:
            current = self.First
            try:
                while current.Next.value != value:
                    if current.Next == None:
                        break
                    else:
                        current = current.Next
                Delete_Nodo = current.Next
                current.Next = Delete_Nodo.Next
            except AttributeError:
                self.size -= 1
        return Delete_Nodo      
    
    def My_pop(self):
        temp = self.First
        while(temp.Next is not None):
            temp = temp.Next
        return temp.data
    
    def __len__(self):
        return self.size

    def __str__(self):
        cad = ""
        current = self.First
        for i in range(len(self)):
            cad += str(current)
            if i != len(self)-1 :
                cad += str(",")
            current = current.Next
        
        return cad
