
# coding: utf-8

# In[4]:


lista=[]
bandera=0
salida=open('/home/mescobar/Escritorio/Lemma_Line_E1.0','w')
with open('/home/mescobar/Escritorio/RI_O_Lemma.conll', 'r') as archivo:
    for line in archivo:
        line=line.split()
        if not(line==[]):  #
            if(line[0]=='.'):
                bandera=1
            if(line[0]=='ri'):
                linea=str(lista)+'\n'
                linea=linea.replace(",","")
                linea=linea.replace("[","")
                linea=linea.replace("]","")
                linea=linea.replace("\'","")
                salida.write(linea)
                lista=[]
            if(line[0]=='other'):
                if bandera:
                    linea=str(lista)+'\n'
                    linea=linea.replace(",","")
                    linea=linea.replace("[","")
                    linea=linea.replace("]","")
                    linea=linea.replace("\'","")
                    salida.write(linea)
                    lista=[]
                    bandera=0
            if(line[0]=='OTHER'):
                if bandera:
                    linea=str(lista)+'\n'
                    linea=linea.replace(",","")
                    linea=linea.replace("[","")
                    linea=linea.replace("]","")
                    linea=linea.replace("\'","")
                    salida.write(linea)
                    lista=[]
                    bandera=0
            if not(line[0]=='ri' or line[0]=='other' or line[0]=='OTHER'):
                lista.append(line[0])
salida.close()

