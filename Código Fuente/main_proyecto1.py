from xml.dom.minidom import DOMImplementation
from xml.dom import NOT_FOUND_ERR, minidom # !Here we have the imports of the libraries for to start the proyect :)
from nodos import *
from Headers import *
#from graphviz import *
from matriz import *
from cargar import *
from LinkedList import *
import os
import xml.etree.ElementTree as ET
from xml.etree import ElementTree


class main_proyecto1():# * i create the principal class  
    menu=0
    terreno_graficar_opcion=0
    canpass1=False
    canpass2=False
    canpass3=False
    canpass4=False
    canpass5=False
    
    # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄        MENÚ PRINCIPAL        ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄  
    def welcome(self):
        print("\033[1;31m"+"████████████████████████████████████████████████████████████████"+'\033[0;m')
        print("\033[1;37m"+"██            ☻☻☻   Welcome to my Project 1   ☻☻☻             ██"+'\033[0;m')
        print("\033[1;37m"+"██           ☻☻☻  Bienvenido a mi Proyecto 1   ☻☻☻            ██"+'\033[0;m')
        print("\033[1;31m"+"████████████████████████████████████████████████████████████████"+'\033[0;m \n')    
    
    def console_menu(self): # * show a principal menu of all the options
        print("\033[1;36m"+"-------------------------------------------------------------------------------------"+'\033[0;m')
        print("\033[1;34m"+"Considere el siguiente MENU para realizar las Funciones del sistema:"+'\033[0;m \n')
        print("\033[1;33m"+"    1.  Cargar Archivo --->"+'\033[0;m')
        print("\033[1;33m"+"    2.  Procesar Archivo (terreno) --->"+'\033[0;m')
        print("\033[1;33m"+"    3.  Escribir Archivo de Salida --->"+'\033[0;m')
        print("\033[1;33m"+"    4.  Mostrar datos del estudiante --->"+'\033[0;m')
        print("\033[1;33m"+"    5.  Generar Gráfica --->"+'\033[0;m')
        print("\033[1;33m"+"    6.  Abrir la documentación --->"+'\033[0;m ')  
        print("\033[1;33m"+"    7.  Salida --->"+'\033[0;m \n') 
        try:
            self.menu=int(input("\033[1;37m"+"Ingrese el número de opción: "+'\033[0;m')) 
            return self.menu 
        except:
            print("\033[1;31m"+"Por favor ingrese un carácter válido"+'\033[0;m')
            self.console_menu()
    
    # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄     CARGA EL ARCHIVO XML     ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄        
    
    names_lands_list=LinkedList() #? los nombres de los terrenos

    posini_x_land_list=LinkedList() #?posiciones iniciales y finales de los recorridos xy
    posfin_x_land_list=LinkedList() 
    posini_y_land_list=LinkedList()
    posfin_y_land_list=LinkedList()

    position_x_list=LinkedList()   #? todas las posiciones de las mega matrices

    position_y_list=LinkedList()

    lagasolinaxd=LinkedList()     #? valor de la gasolina de las matrices
    
    dimension_list_x=LinkedList()  #?dimensiones de la matriz

    dimension_list_y=LinkedList()  

    contador_terrenos=0


    def cargarxml(self):        # ! 1.  Cargar Archivo --->
       
        # ? Aqui se carga el archivo XML completo
        try:
            #entrada=input("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Ingrese la ruta del Archivo  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')
            entrada=r"C:\Users\Sr. C\Desktop\Archivo prueba.xml"
            myxml=ET.parse(entrada)

            root=myxml.getroot()

            strmyxml=ET.tostring(root, encoding='utf8', method='xml')
            
            strmyxml=strmyxml.lower()
           
            myxml = minidom.parseString(strmyxml)
            
            lands_all=myxml.getElementsByTagName('terrenos')    # * se guarda en una variable todo el xml
                    

            for lands in lands_all:    # ? FOR que recorre todos los terrenos                      
               
                land_all = lands.getElementsByTagName('terreno') 
                
                # if len(land_all) == 0:                
                #     land_all=myxml.getElementsByTagName('Terreno')
                # elif len(land_all)==0:
                #     land_all=myxml.getElementsByTagName('TERRENO')
                # else:
                #     land_all=myxml.getElementsByTagName('tERRENO')
 
                # if land_all is None:
                #     print(True)
                # else:
                    # print(False)
                for land in land_all:    # ? For que recorre cada uno de los terrenos
                    position_Matriz=matriz()
                    
                    self.contador_terrenos += 1
                    land_name = land.getAttribute('nombre')
                    self.names_lands_list.My_Append(land_name) 

                    dimension = land.getElementsByTagName('dimension')[0]        # ? posicion inicial
                    # if len(lands_all) == "0":                
                    #     dimension=myxml.getElementsByTagName('DIMENSION')[0] 
                    # elif len(lands_all)=="0":
                    #     dimension=myxml.getElementsByTagName('Dimension')[0] 
                    # else:
                    #     dimension=myxml.getElementsByTagName('dIMENSION')[0] 
                        
                    dimension_x = dimension.getElementsByTagName('m')[0].firstChild.nodeValue                    
                    dimension_y = dimension.getElementsByTagName('n')[0].firstChild.nodeValue
                    
                    if (int(dimension_x)>100) or (int(dimension_y)>100):
                        print("\033[1;31m"+"Las dimensiones de algun terreno no son correctas, deben ser menores o iguales a 100"+'\033[0;m')
                        print("\033[1;31m"+"\n por no considerarlo se termina el programa bye :)"+'\033[0;m')
                        exit()

                    self.dimension_list_x.My_Append(dimension_x)
                    self.dimension_list_y.My_Append(dimension_y)

                    posini = land.getElementsByTagName('posicioninicio')[0]        # ? posicion inicial    
                    posini_x = posini.getElementsByTagName('x')[0].firstChild.nodeValue                    
                    posini_y = posini.getElementsByTagName('y')[0].firstChild.nodeValue
                    
                    posfin = land.getElementsByTagName('posicionfin')[0]           # ? posicion final    
                    posfin_x = posfin.getElementsByTagName('x')[0].firstChild.nodeValue
                    posfin_y = posfin.getElementsByTagName('y')[0].firstChild.nodeValue

                    print("\033[1;36m"+"\n NOMBRE DEL TERRENO:       ", land_name +'\033[0;m')
                    print("\033[1;33m"+"\n posición inicial:  (",posini_x,",",posini_y,")\n"+'\033[0;m')
                    print("\033[1;33m"+" posicion final:  (",posfin_x,",",posfin_y,")\n"+'\033[0;m')                  
                    
                    
                    # todo guardo en las posiciones INICIALES Y FINALES en listas creadas por mi
                    self.posini_x_land_list.My_Append(posini_x) #*posicion inicial  X
                    self.posini_y_land_list.My_Append(posini_y) #*posicion inicial  Y                  
                    self.posfin_x_land_list.My_Append(posfin_x) #*posicion final  X                  
                    self.posfin_y_land_list.My_Append(posfin_y) #*posicion final  Y 

                    position_gas=land.getElementsByTagName('posicion') # ? aqui se extraen los atributos de las posiciones de toda la cuadrícula 
                    for positionunit in position_gas:
                        
                        position_x=positionunit.getAttribute('x') #* extraigo las X de posicion
                        position_y=positionunit.getAttribute('y')  #* extraigo las Y de posicion
                        #print("\033[1;37m"+"     Posicion:  (",position_x,",",position_y,")"+'\033[0;m')
                        self.position_x_list.My_Append(int(position_x)) #* agrego las X Y en mi lista que cree para guardarlas
                        self.position_y_list.My_Append(int(position_y))
                        gasolinas = positionunit.firstChild.nodeValue #* OJO aqui obtengo los valores de la gasolina de cada coordenada.
                        gasolina = str(gasolinas)                        
                        self.lagasolinaxd.My_Append(gasolina)
                        #print("\033[1;37m"+"         ",gasolina," "+'\033[0;m')
                        # ! probando utilizar la matriz ortogonal:
                        
                        position_Matriz.insert(int(position_x),int(position_y),gasolina)
                        


                    #print("\033[1;37m"+"fila, columna, valor de gas"+'\033[0;m')

                    position_Matriz.recorrerows()

            global positions_ordered_x
            global positions_ordered_y
            global fuels_ordered

            print("\n \n ")
            print("--------------------------------------------------------------")
            # print("POSICIÓN INICIAL COORD. X:  ",str(self.posini_x_land_list))
            # print("POSICIÓN INICIAL COORD Y:  ",str(self.posini_y_land_list))
            # print("POSICION FINAL COORD X: ",str(self.posfin_x_land_list))
            # print("POSICION FINAL COORD Y: ",str(self.posfin_y_land_list))
            # print("POSICIONES COORD X: ",str(positions_ordered_x))
            # print("POSICIONES COORD Y: ",str(positions_ordered_y))
            # print("LA GASOLINA : ",str(fuels_ordered))

            # # ? ahora por asi decirlo serializo mis datos.
            # posinix = open('serializables/posicion_inicial_x.txt', 'w')
            # posiniy = open('serializables/posicion_inicial_y.txt', 'w')
            # posfinx = open('serializables/posicion_final_x.txt', 'w')
            # posfiny = open('serializables/posicion_final_y.txt', 'w')
            # posx = open('serializables/posicion_x.txt', 'w')
            # posy = open('serializables/posicion_y.txt', 'w')
            # gaso = open('serializables/la_Gasolina.txt', 'w')

            # try:
            #     with open('serializables/posicion_inicial_x.txt', 'w') as f:
            #         posinix.write(str(self.posini_x_land_list))

            #     with open('serializables/posicion_inicial_y.txt', 'w') as f:
            #         posiniy.write(str(self.posini_y_land_list)) 

            #     with open('serializables/posicion_final_x.txt', 'w') as f:
            #         posfinx.write(str(self.posfin_x_land_list))

            #     with open('serializables/posicion_final_y.txt', 'w') as f:
            #         posfiny.write(str(self.posfin_y_land_list))

            #     with open('serializables/posicion_x.txt', 'w') as f:
            #         posx.write(str(self.position_x_list))

            #     with open('serializables/posicion_y.txt', 'w') as f:
            #         posy.write(str(self.position_y_list)) 

            #     with open('serializables\la_Gasolina.txt', 'w') as f:
            #         gaso.write(str(self.lagasolinaxd))
                                
            # finally:
            #     posinix.close()
            #     posiniy.close()
            #     posfinx.close()
            #     posfiny.close()
            #     posx.close()
            #     posy.close()
            
            self.canpass1=True
            
            print("\033[1;32m"+"  MENSAJE:       El archivo se cargó con éxito!"+'\033[0;m')
            
            '''DOMimpl = minidom.getDOMImplementation()
            xmldoc=DOMimpl.createDocument(None, "terrenos", None)
            doc_root= xmldoc.documentElement
            for lands in lands_all:'''
            

        except Exception as e:
            print("\033[1;31m"+"     MENSAJE:   Por favor verifique la ruta de su archivo, gracias c:"+'\033[0;m')
            print(e)
            self.console_menu()               
   

    def ordenar_in_Nodes(self, value):
        Ld=matriz()
        listxtostr=str(self.dimension_list_x)
        print(listxtostr)
        listytostr=str(self.dimension_list_y)
        print(listytostr)

        posinixx=str(self.position_x_list)
        
        posiniy=str(self.position_y_list)
        
        gasofa=str(self.lagasolinaxd)
        
        posini_x=str(self.posini_x_land_list)
        posini_y=str(self.posini_y_land_list)
        posfin_x=str(self.posfin_x_land_list)
        posfin_y=str(self.posfin_y_land_list)

        m=listxtostr.split(",") 
        print(m)       
        n=listytostr.split(",")
        x=posinixx.split(",")
        y=posiniy.split(",")

        xo=posini_x.split(",")
        xf=posfin_x.split(",")
        yo=posini_y.split(",")
        yf=posfin_y.split(",")

        gas=gasofa.split(",")
        # acum=0        
        # #*prueba del comtador
        # for i in range(self.contador_terrenos):
        #     print("acum:  ",acum)
        #     acum2=0
        #     print("TERRENO NO. ",i+1)
        #     print("int(m[i])*int(n[i])  ",int(m[i])," ",int(n[i]),"=",int(m[i])*int(n[i]))
        #     for l in range(acum,int(m[i])*int(n[i])+acum):                              
        #         print(l)
        #         acum2 +=1                
        #     acum +=acum2
        
        

        acum=0
        print("     TERRENO NO. ",value+1)
        print(m[value])
        print(n[value])
        print("Inicio: ",xo[value],",",yo[value])
        print("Final: ",xf[value],",",yf[value])
        for i in range(self.contador_terrenos):
            acum2=0
            print(acum)
            for l in range(acum,int(m[i])*int(n[i])+acum): 
                if int(value)==int(i):
                    Ld.insert(x[l], y[l],gas[l])
                acum2 +=1
            acum +=acum2

        Ld.recorrerows()
        Ld.optimize_ways(xo[value],yo[value],xf[value],yf[value],m[value],n[value])
        self.writexmlsalida(value,xo[value],yo[value],xf[value],yf[value])
        
    # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄    PROCESA EL ARCHIVO XML    ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
    def processfile(self):      # ! 2.  Procesar Archivo --->
        print("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  PROCESO DEL ARCHIVO  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')
        print("\n \033[1;36m"+"Por favor seleccione el terreno que desea PROCESAR: "+'\033[0;m  \n')
        #print(str(self.names_lands_list))
        self.names_lands_list=str(self.names_lands_list)
        #?aqui va el for para los terrenos
        i=1
        for l in self.names_lands_list.split(","):
            print("\033[1;33m"+"        ",i,".  "+str(l)+" --->"+'\033[0;m \n')
            i=i+1

        try:
            self.terreno_PROCESAR_opcion=int(input("\033[1;37m"+"Por favor con el identificador seleccione el terreno que desea graficar: "+'\033[0;m')) 
            listoption = self.names_lands_list.split(",")
            option = listoption[int(self.terreno_PROCESAR_opcion)-1]
            if option in self.names_lands_list.split(","):
                
                option=str(option)
                #print("si esta y es: "+ option)
                self.ordenar_in_Nodes(int(self.terreno_PROCESAR_opcion)-1)
                #self.crear_grafico_selected()

                # todo:  llamo a un método que me imprima en graphviz una imagen del terreno seleccionado


            else:
                print("\033[1;31m"+"El valor que ingresó no se encuentra, verifiquelo! :("+'\033[0;m')
                self.processfile()
        except Exception as e:
            print("\033[1;31m"+"Por favor ingrese un carácter válido :("+'\033[0;m')
            print(e)
            self.processfile()
    

    # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄    ESCRIBE EL ARCHIVO XML    ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
    
    def indent(self, elem, level=0):
        i = "\n" + level*"  "
        j = "\n" + (level-1)*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                self.indent(subelem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = j
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = j
        return elem   

    def writexmlsalida(self, value,xo, yo, xf,  yf):
        global positions_ordered_x
        global positions_ordered_y
     
        # global gasolinavale
        global gasolinalista
        global coordenadalistax
        global coordenadalistay
        global gasolinalistafull  
        
        posini_x=str(self.posini_x_land_list)
        posini_y=str(self.posini_y_land_list)
        posfin_x=str(self.posfin_x_land_list)
        posfin_y=str(self.posfin_y_land_list)
       
        gasolistaa=str(gasolinalista).split(",")
        coorlistax=str(coordenadalistax).split(",")
        coorlistay=str(coordenadalistay).split(",")
        gasolinalistafull=str(gasolinalistafull)


        acum=0   
        acum2=0  


                
        print("TERRENO NO. ",value+1)
        terrenos = ET.Element('terrenos')

        terrenos.set('name',self.names_lands_list.split(",")[value])

        posicioninicio = ET.SubElement(terrenos, 'posicioninicio')
        ET.SubElement(posicioninicio, 'x').text=xo
        ET.SubElement(posicioninicio, 'y').text=xf

        posicionfin = ET.SubElement(terrenos, 'posicionfin')
        ET.SubElement(posicionfin, 'x').text=yo
        ET.SubElement(posicionfin, 'y').text=yf
    
        ET.SubElement(terrenos, 'combustible').text=str(gasolinalistafull)

        
            
        if len(coorlistax)== len(gasolistaa):
                
            for r in range(len(coorlistax)):

                ET.SubElement(terrenos, 'posicion', x=str(coorlistax[int(r)]), y=str(coorlistay[r])).text=gasolistaa[r]
    
        

        # try:
            
        
        valor=str(int(value)+1)
        
        archivo = open('XML_generados/archivo_Salida_'+valor+'.xml','w')

        mydata=ET.tostring(self.indent(terrenos), encoding='utf-8').decode('utf-8')

        archivo.write(mydata)
            
        # except Exception:
        #     print("\033[1;31m"+"\nUps... algo salió mal :( podria haber un error, intentelo nevamente\n"+'\033[0;m')     
        #     return False
    
    def obtain_from_files_xml(self, value):
        try:
            os.startfile(r"XML_generados\archivo_Salida_"+str(int(value)+1)+".xml")
            print("\033[1;32m"+"\nSe ha generado el XML " +str(int(value)+1)+ "con éxito... \n"+'\033[0;m')

        except Exception as e:
            print("\033[1;31m"+"\nNo se puede Generar un XML vacío (o que no haya procesado) asegurese haya procesado el terreno\n"+'\033[0;m')     
            print(e)
            self.console_menu()
            return False

    def write_outfile(self):    # ! 3.  Escribir Archivo de Salida --->
        print("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Escribiendo archivo de salida  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')
        

        print("\n \033[1;36m"+"Por favor seleccione el terreno a escribir XML: "+'\033[0;m  \n')
        #print(str(self.names_lands_list))
        self.names_lands_list=str(self.names_lands_list)
        #?aqui va el for para los terrenos
        i=1
        for l in self.names_lands_list.split(","):
            print("\033[1;33m"+"        ",i,".  "+str(l)+" --->"+'\033[0;m \n')
            i=i+1

        # try:
        self.terreno_PROCESAR_opcion=int(input("\033[1;37m"+"Por favor con el identificador seleccione el terreno que desea graficar: "+'\033[0;m')) 
        listoption = self.names_lands_list.split(",")
        option = listoption[int(self.terreno_PROCESAR_opcion)-1]
        if option in self.names_lands_list.split(","):
            
            option=str(option)
            #print("si esta y es: "+ option)
            self.obtain_from_files_xml(int(self.terreno_PROCESAR_opcion)-1)
            
            #self.crear_grafico_selected()

            # todo:  llamo a un método que me imprima en graphviz una imagen del terreno seleccionado


        else:
            print("\033[1;31m"+"El valor que ingresó no se encuentra, verifiquelo! :("+'\033[0;m')
            self.write_outfile()
        # except Exception as e:
        #     print("\033[1;31m"+"Por favor ingrese un carácter válido :("+'\033[0;m')
        #     print(e)
            # self.write_outfile()

    
    # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄      MUESTRA MIS DATOS       ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
    def show_my_data(self):     # ! 4.  Mostrar datos del estudiante --->
        print("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Mis datos personales  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')   
        print("\033[1;32m"+"  •  Alvaro Emmanuel Socop Pérez"+'\033[0;m')
        print("\033[1;32m"+"  •  202000194"+'\033[0;m')
        print("\033[1;32m"+"  •  Introducción a la programación y computación 2 sección E"+'\033[0;m')
        print("\033[1;32m"+"  •  Ingeniería en Ciencias y Sistemas"+'\033[0;m')  
        print("\033[1;32m"+"  •  4to. Semestre"+'\033[0;m \n')  
        #self.position_Matriz.recorrerows()    

    
    # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄       GENERA GRÁFICA         ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
    def crear_grafico_selected(self, value):
        global positions_ordered_x
        global positions_ordered_y
        global fuels_ordered
        print(print("\033[1;37m"+"De acuerdo a la consideración: "+'\033[0;m'))
        print("\033[1;36m"+"\" implementar una lista simplemente enlazada, creada por el estudiante, creando una clase Nodo y una clase lista, de tal manera que al recorrer la lista se pueda validar la existencia de los nombres de los mapas \""+'\033[0;m')
        print(print("\033[1;37m"+"Se recorre la lista creada por mi: "+'\033[0;m'))
        print("names_lands_list:")
        
        print("\033[1;36m"+"mi lista en string: "+str(self.names_lands_list)+'\033[0;m')
        graphtext3=""
        graphtext="""
        graph grid{
	            layout=dot   
                fontcolor="white" 
                label=" Terreno   """+str(int(value)+1)+"""    "    
                labelloc = "t"
                bgcolor="blue:orange"    
                edge [weight=1000 style=radial color=black ]
                node [shape=circle style="filled"  color="green:cyan" gradientangle="315"]
                
                edge [weight=1000 style=bold color=black]\n
                """

        graphtext2="""
        graph grid
        {   layout=dot   
            fontcolor="white" 
            label="Terreno """+str(int(value)+1)+""""    
            labelloc = "t"
            bgcolor="blue:orange"    
            edge [weight=1000 style=radial color=white border="10"]
            node [shape=circle style=filled color=black]
            \n   
            	
            a0 [label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="yellow:violet" gradientangle="315">
            <TR>
        """
        # positionsx=str(positions_ordered_x)
        # print(positionsx)
        # positionsy=str(positions_ordered_y)
        # print(positionsy)

        # posinix=str(self.position_x_list)
        
        # posiniy=str(self.position_y_list)
        
        gasofa=str(fuels_ordered)
        dimensionx=str(self.dimension_list_x).split(',')
        dimensiony=str(self.dimension_list_y).split(',')
        # m=positionsx.split(",")        
        # n=positionsy.split(",")
        # x=posinix.split(",")
        # y=posiniy.split(",")
        gas=gasofa.split(",")
        acum=0        
        ac=0
        ac2=0  
        ac3=0
        st=1
        st2=1
        acum2=0  
        emme=0
        contador=0
        stt=1
        st2t=1
        emmet=0
        for i in range(self.contador_terrenos):
            acum2=0
            acum3=0
            acc=0  
            acc=0
            # print("TERRENO NO. ",i+1)
            # print("value:  ",value)
            # print("i: ",i )

            eme=int(dimensionx[i])
            ene=int(dimensiony[i])

            for l in range(acum,int(eme)*int(ene)+acum):
                if int(value)==int(i):                     
                    if ac2<int(ene):
                        ac2 +=1
                        graphtext+="    "+str(acc+1)+" [ label=\""+str(gas[l])+"\" ]; \n "
                        # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
                    else:
                        graphtext+="    "+str(acc+1)+" [ label=\""+str(gas[l])+"\" ]; \n "
                        ac2=1
                        # graphtext2+="</TR>\n<TR>"
                        # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
                acc+=1         
                

            if int(value)==int(i):
                graphtext+="rank=same { "
            for w in range(acum,int(eme)*int(ene)+acum):
                if int(value)==int(i):

                    if ac<int(ene):
                        ac +=1
                        graphtext+=str(acum2+1)+"--"
                        # graphtext3+=str(st+emme)+"--"
                        # st+=eme
                        emme+=eme 
                        # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
                    else:
                        ac=1
                        st2+=1
                        emme=st2
                        graphtext=graphtext.rstrip(graphtext[-1])
                        # graphtext3=graphtext3.rstrip(graphtext3[-1])
                        graphtext+="}\n rank=same {"
                        graphtext+=str(acum2+1)+"--"
                        # graphtext3+="\n"+str(emme)+"--"
                        emme+=eme-1
                        # graphtext2+="</TR>\n<TR>"
                        # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
                        
                acum2 +=1



            for t in range(acum,int(eme)*int(ene)+acum):
                if int(value)==int(i):

                    if ac3<int(eme):
                        ac3 +=1
                        
                        graphtext3+=str(stt+emmet)+"--"
                        # st+=eme
                        emmet+=ene 
                        # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
                    else:
                        ac3=1
                        st2t+=1
                        emmet=st2t
                        
                        graphtext3=graphtext3.rstrip(graphtext3[-1])
                        
                        
                        graphtext3+="\n"+str(emmet)+"--"
                        emmet+=ene-1
                        # graphtext2+="</TR>\n<TR>"
                        # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
                        
                acum3 +=1



            
            if int(value)==int(i):
                graphtext=graphtext.rstrip(graphtext[-1]) 
                graphtext3=graphtext3.rstrip(graphtext3[-1]) 
                graphtext+="}\n"




            # for z in range(acum,int(eme)*int(ene)+acum):
            #     if int(value)==int(i):
            #         if ac3<int(ene):
            #             ac3 +=1
            #             graphtext+=str(i+1)+"--"
            #             # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
            #         else:
            #             ac3=1
            #             graphtext=graphtext.rstrip(graphtext[-1])
            #             graphtext+="}\n "
            #             # graphtext2+="</TR>\n<TR>"
            #             # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
               
            acum +=acum2
        # print(graphtext2)

        try:
            
            # graphtext2 = graphtext2[:-4]
            # graphtext2 += "</TR>\n</TABLE>>];}"
            graphtext+=graphtext3
            graphtext+="}"
            valor=str(int(value)+1)
            file=open('Graficos_generados/Grafico_'+valor+'.dot','w')
            file.write(graphtext)
            file.close()

            os.system("dot -Tpng Graficos_generados/Grafico_"+str(int(value)+1)+".dot -o Graficos_generados/grafico_"+str(int(value)+1)+".png")
            os.startfile(r"Graficos_generados\grafico_"+str(int(value)+1)+".png")
            print("\033[1;32m"+"\nSe ha generado el gráfico" +str(int(value)+1)+ "con éxito... \n"+'\033[0;m')
        except Exception:
            print("\033[1;31m"+"\nUps... algo salió mal :( podria haber un error, intentelo nevamente\n"+'\033[0;m')     
            return False

    def gen_graphic(self):      # ! 5.  Generar Gráfica --->
        print("\n \033[1;33m"+"↓↓↓↓↓↓↓↓↓  Generando Gráfica  ↓↓↓↓↓↓↓↓↓"+'\033[0;m  \n')
        print("\n \033[1;36m"+"Por favor seleccione el terreno que desea graficar: "+'\033[0;m  \n')
        #print(str(self.names_lands_list))
        self.names_lands_list=str(self.names_lands_list)
        #?aqui va el for para los terrenos
        i=1
        for l in self.names_lands_list.split(","):
            print("\033[1;33m"+"        ",i,".  "+str(l)+" --->"+'\033[0;m \n')
            i=i+1

        try:
            self.terreno_graficar_opcion=int(input("\033[1;37m"+"Por favor con el identificador seleccione el terreno que desea graficar: "+'\033[0;m')) 
            listoption = self.names_lands_list.split(",")
            option = listoption[int(self.terreno_graficar_opcion)-1]
            if option in self.names_lands_list.split(","):
                
                option=str(option)
                print("si esta y es: "+ option)
                self.crear_grafico_selected(int(self.terreno_graficar_opcion)-1)

                # todo:  llamo a un método que me imprima en graphviz una imagen del terreno seleccionado


            else:
                print("\033[1;31m"+"El valor que ingresó no se encuentra, verifiquelo! :("+'\033[0;m')
                self.gen_graphic()
        except Exception as e:
            print("\033[1;31m"+"Por favor ingrese un carácter válido :("+'\033[0;m')
            print(e)
            self.gen_graphic()


    # todo▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄       GENERA GRÁFICA         ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ ▀▄▀▄ ▀▄▀▄ 
    # todo:  CONDICIONES DEL MENU
    def Principal_menu(self):
        self.welcome()
        while(self.menu!=7):           
            self.menu=self.console_menu()
            
            if self.menu == 1: # ! 1.  Cargar Archivo --->
                print("\033[1;36m"+"...  Analizando el archivo .lfp ..."+'\033[0;m')
                self.cargarxml()                    
                print("")
                
            if self.menu == 2: # ! 2.  Procesar Archivo --->
                self.canpass1=True
                if self.canpass1:
                    
                    self.processfile()

                    self.canpass2=True
                else:
                    print("\033[1;31m"+"Por favor siga un orden :)"+'\033[0;m')

            if self.menu == 3: # ! 3.  Escribir Archivo de Salida --->
                if self.canpass2:

                    self.write_outfile()

                    self.canpass3=True
                else:
                    print("\033[1;31m"+"Por favor siga un orden :)"+'\033[0;m')
            if self.menu == 4: # ! 4.  Mostrar datos del estudiante --->
                
                self.show_my_data()
                    
            if self.menu == 5: # ! 5. Generar Gráfica  --->
                if self.canpass2:

                    self.gen_graphic()
                else:
                    print("\033[1;31m"+"Por favor siga un orden :)"+'\033[0;m')
                    print("\033[1;31m"+"    O Verifique que ya haya cargado terrenos primero, gracias"+'\033[0;m')
            
            if self.menu == 6: # ! 5.  Mostrar la documentación --->                
                os.startfile(r"Documentacion\202000194_Ensayo_LAB.pdf")
                print("\033[1;32m"+"\n      Se ha Abierto el PDF  con éxito... \n"+'\033[0;m')


        print("\033[1;36m"+"██████████████████████████████████████████████████████████████████"+'\033[0;m')    
        print("\033[1;36m"+"███████████████████████  FIN DEL PROGRAMA  ███████████████████████"+'\033[0;m')
        print("\033[1;36m"+"██████████████████████████████████████████████████████████████████"+'\033[0;m')
        exit()



if __name__ == '__main__': 
    p1=main_proyecto1()
    p1.Principal_menu()



# todos mis colorcitos c:
def colorestext():
    print("")   
    print("\033[1;36m"+"Texto en negrita color CYAN"+'\033[0;m')
    print("\033[1;37m"+"Texto en negrita color BLANCO"+'\033[0;m')
    print("\033[1;33m"+"Texto en negrita color amarillo"+'\033[0;m')
    print("\033[1;32m"+"Texto en negrita color VERDE"+'\033[0;m')
    print("\033[1;31m"+"Texto en negrita color ROJO"+'\033[0;m')
    print("\033[1;34m"+"Texto en negrita color AZUL"+'\033[0;m')

