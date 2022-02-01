
lista2=[]
def muotoile(lista):
    lista2=[]
    i=0
    for i in lista:
        lista2.append(f"{i:.2f}")
    
    return lista2
       
      


if __name__=="__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)





    