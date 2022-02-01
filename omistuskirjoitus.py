nimi = input("Kenelle teos omistetaan: ")
mihin = input("mihin kirjoitetaan:")

with open(mihin, "w") as tiedosto:
    print("jooseppi laulaa")
    print("tama on muutos")
    print(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")
