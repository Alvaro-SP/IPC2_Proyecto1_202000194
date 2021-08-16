class thenodo():
    def __init__(self, valor):
        self.value = valor
        self.Next = None
    def __str__(self):
        return str(self.value)

graphtext=""
ene=5
eme=0
ac=0
st=1
st2=1
graphtext3=""
graphtext+="rank=same {"
for l in range(25):
    if int(0)==int(0):

        if ac<int(ene):
            ac +=1
            
            graphtext+=str(l+1)+"--"
            graphtext3+=str(st+eme)+"--"
            st+=eme
            eme=ene  
            # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
        else:
            ac=1
            st2+=1
            st=st2
            graphtext=graphtext.rstrip(graphtext[-1])
            graphtext3=graphtext3.rstrip(graphtext3[-1])

            graphtext+="}\n rank=same {"
            graphtext+=str(l+1)+"--"
            
            graphtext3+="\n"+str(st)+"--"
            
           
            
            
            
            # graphtext2+="</TR>\n<TR>"
            # graphtext2+="<TD border=\"3\"  bgcolor=\"green:cyan\" gradientangle=\"315\">"+str(gas[l])+"</TD>\n"
graphtext=graphtext.rstrip(graphtext[-1]) 
graphtext+="}"
print(graphtext)   
print(graphtext3)  