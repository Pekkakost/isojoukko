def lue_sanakirja():

    sanakirja=[]


    with open("sanakirja.txt")as tiedosto:
        for rivi in tiedosto:
            rivi=rivi.replace("\n","")
            sanakirja.append(tuple(rivi.split(";")))

    return sanakirja

def lisää_sana(sanakirja: list):
    sana_fi = input("Anna sana suomeksi: ")
    sana_eng = input("Anna sana englanniksi: ")
    # Lisätään listaan
    sanakirja.append((sana_fi, sana_eng))

    with open("sanakirja.txt","a")as tiedosto:
        tiedosto.write(sana_fi +";"+sana_eng+"\n")
        print("sanapari lisätty")

def hae_sana(sanakirja:list):
    sana=input("mikä sana:")
    for sana_fi,sana_eng in sanakirja:
        if sana in sana_fi or sana in sana_eng:
            print(f"{sana_fi} - {sana_eng}")



sanakirja=lue_sanakirja
while True:
    print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
    valinta=input("valinta: ")
    
    if valinta == "1":
        lisää_sana(sanakirja)
    elif valinta == "2":
        hae_sana(sanakirja)

    elif valinta == "3":
        print("Moi")
        break



#if __name__=="__main__":
 #   lue_sanakirja()