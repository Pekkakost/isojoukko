def pisin_naapurijono(lista):
    uusi=[]
    pituus=0
    for i in lista:
        #if i-(i+1)==1 or i-(i+1)==-1:
        if lista[i+1]==1 or lista[i-1]==1:
            #if alkio - (alkio+1) == 1 or alkio - (alkio+1) == -1:
            uusi.append(i)
            pituus=len(uusi)

    return uusi,pituus

if __name__=="__main__":
    lista = [1, 2, 5, 4, 3, 4]
    print(pisin_naapurijono(lista))