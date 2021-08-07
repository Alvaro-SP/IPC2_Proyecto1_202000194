if __name__ == '__main__':

    from xml.dom import minidom # !Here we have the imports of the libraries for to start the proyect :)
    class thenodo():
        def __init__(self, valor):
            self.value = valor
            self.Next = None
        def __str__(self):
            return str(self.value)

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
        
        def __len__(self):
            return self.size

        def __str__(self):
            cad = "["
            current = self.First
            for i in range(len(self)):
                cad += str(current)
                if i != len(self)-1 :
                    cad += str(",")
                current = current.Next
            cad += "]"
            return cad
 
    class main_proyecto1():# * i create the welcome menu
        # TODO: MÉTODOS 
        menu=0
        canpass1=False
        canpass2=False
        canpass3=False
        canpass4=False
        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄        MENÚ PRINCIPAL        ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄  
        def welcome(self):
            print("\033[1;31m"+"████████████████████████████████████████████████████████████████"+'\033[0;m')
            print("\033[1;37m"+"██            ☻☻☻   Welcome to my Project 1   ☻☻☻             ██"+'\033[0;m')
            print("\033[1;37m"+"██           ☻☻☻  Bienvenido a mi Proyecto 1   ☻☻☻            ██"+'\033[0;m')
            print("\033[1;31m"+"████████████████████████████████████████████████████████████████"+'\033[0;m \n')    
        
        def console_menu(self): # * show a principal menu of all the options
            
            print("\033[1;34m"+"Considere el siguiente MENU para realizar las Funciones del sistema:"+'\033[0;m \n')
            print("\033[1;33m"+"    1.  Cargar Archivo --->"+'\033[0;m')
            print("\033[1;33m"+"    2.  Procesar Archivo --->"+'\033[0;m')
            print("\033[1;33m"+"    3.  Escribir Archivo de Salida --->"+'\033[0;m')
            print("\033[1;33m"+"    4.  Mostrar datos del estudiante --->"+'\033[0;m')
            print("\033[1;33m"+"    5.  Generar Gráfica --->"+'\033[0;m')
            print("\033[1;33m"+"    6.  Salida --->"+'\033[0;m \n')  
            try:
                self.menu=int(input("\033[1;37m"+"Ingrese el número de opción: "+'\033[0;m')) 
                return self.menu 
            except:
                print("\033[1;31m"+"Por favor ingrese un carácter válido"+'\033[0;m')
                self.console_menu()

        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄     CARGA EL ARCHIVO XML     ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄        
        def cargarxml(self):        # ! 1.  Cargar Archivo --->
            # ? Aqui se carga el archivo XML completo
            try:
                myxml=minidom.parse(input("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Ingrese la ruta del Archivo  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n'))            
                lands_all=myxml.getElementsByTagName('terrenos')    # * se guarda en una variable todo el xml
                
                for lands in lands_all:    # ? FOR que recorre todos los terrenos            
                    land_all = lands.getElementsByTagName('terreno')  
                    
                    for land in land_all:    # ? For que recorre cada uno de los terrenos
                        land_name = land.getAttribute('nombre')
                        
                        posini = land.getElementsByTagName('posicioninicio')[0]        # ? posicion inicial    
                        posini_x = posini.getElementsByTagName('x')[0].firstChild.nodeValue                    
                        posini_y = posini.getElementsByTagName('y')[0].firstChild.nodeValue
                        
                        posfin = land.getElementsByTagName('posicionfin')[0]           # ? posicion final    
                        posfin_x = posfin.getElementsByTagName('x')[0].firstChild.nodeValue
                        posfin_y = posfin.getElementsByTagName('y')[0].firstChild.nodeValue
                        print("\033[1;36m"+"\n El terreno es: ", land_name +'\033[0;m')
                        print("\033[1;33m"+"\n posición inicial:  (",posini_x,",",posini_y,")", "\n posicion final:  (",posfin_x,",",posfin_y,")\n"+'\033[0;m')                   
                            
                        position_gas=land.getElementsByTagName('posicion') # ? aqui se extraen los atributos de las posiciones de toda la cuadrícula 
                        for positionunit in position_gas:
                            position_x=positionunit.getAttribute('x')
                            position_y=positionunit.getAttribute('y')
                            print("\033[1;37m"+"     Posicion:  (",position_x,",",position_y,")"+'\033[0;m')
                self.canpass1=True
                print("\033[1;32m"+"  MENSAJE:       El archivo se cargó con éxito!"+'\033[0;m')
            except:
                print("\033[1;31m"+"     MENSAJE:   Por favor verifique la ruta de su archivo, gracias c:"+'\033[0;m')
                self.console_menu()               
        
        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄    PROCESA EL ARCHIVO XML    ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
        def processfile(self):      # ! 2.  Procesar Archivo --->
            print("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Se está procesando el archivo  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')

        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄    ESCRIBE EL ARCHIVO XML    ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
        def write_outfile(self):    # ! 3.  Escribir Archivo de Salida --->
            print("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Escribiendo archivo de salida  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')
        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄      MUESTRA MIS DATOS       ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
        def show_my_data(self):     # ! 4.  Mostrar datos del estudiante --->
            print("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Mis datos personales  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')   
            print("\033[1;32m"+"  •  Alvaro Emmanuel Socop Pérez"+'\033[0;m')
            print("\033[1;32m"+"  •  202000194"+'\033[0;m')
            print("\033[1;32m"+"  •  Introducción a la programación y computación 2 sección E"+'\033[0;m')
            print("\033[1;32m"+"  •  Ingeniería en Ciencias y Sistemas"+'\033[0;m')  
            print("\033[1;32m"+"  •  4to. Semestre"+'\033[0;m \n')      

        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄       GENERA GRÁFICA         ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
        def gen_graphic(self):      # ! 5.  Generar Gráfica --->
            print("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Generando Gráfica  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')

        # TODO: CONDICIONES DEL MENU
        def conditions_menu(self):
            self.welcome()
            while(self.menu!=6):           
                self.menu=self.console_menu()
                
                if self.menu == 1: # ! 1.  Cargar Archivo --->
                    print("\033[1;36m"+"...  Analizando el archivo .lfp ..."+'\033[0;m')
                    self.cargarxml()                    
                    print("")
                    
                    
                if self.menu == 2: # ! 2.  Procesar Archivo --->
                    if self.canpass1:



                        self.canpass2=True
                    else:
                        print("\033[1;31m"+"Por favor siga un orden :)"+'\033[0;m')

                if self.menu == 3: # ! 3.  Escribir Archivo de Salida --->
                    if self.canpass2:



                        self.canpass3=True
                    else:
                        print("\033[1;31m"+"Por favor siga un orden :)"+'\033[0;m')
                if self.menu == 4: # ! 4.  Mostrar datos del estudiante --->
                   
                    self.show_my_data()
                        
                if self.menu == 5: # ! 5.  Generar Gráfica --->
                    if self.canpass3:

                        pass
                    else:
                        print("\033[1;31m"+"Por favor siga un orden :)"+'\033[0;m')

            print("\033[1;36m"+"██████████████████████████████████████████████████████████████████"+'\033[0;m')    
            print("\033[1;36m"+"███████████████████████  FIN DEL PROGRAMA  ███████████████████████"+'\033[0;m')
            print("\033[1;36m"+"██████████████████████████████████████████████████████████████████"+'\033[0;m')
            exit()
    p1=main_proyecto1()
    p1.conditions_menu()

def colorestext():
    print("")   
    print("\033[1;36m"+"Texto en negrita color CYAN"+'\033[0;m')
    print("\033[1;37m"+"Texto en negrita color BLANCO"+'\033[0;m')
    print("\033[1;33m"+"Texto en negrita color amarillo"+'\033[0;m')
    print("\033[1;32m"+"Texto en negrita color VERDE"+'\033[0;m')
    print("\033[1;31m"+"Texto en negrita color ROJO"+'\033[0;m')
    print("\033[1;34m"+"Texto en negrita color AZUL"+'\033[0;m')

