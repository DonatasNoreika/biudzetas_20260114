from saskaita import BankoSaskaita

saskaita = BankoSaskaita("Vardenis")
if __name__ == "__main__":
    while True:
        veiksmas = int(input("1 - pridėti, 2 - išimti, 3 - balansas, 4 - peržiūrėti, 0 - išeiti: "))
        match veiksmas:
            case 1:
                suma = abs(float(input("Suma: ")))
                siuntejas = input("Siuntėjas: ")
                info = input("Papildoma informacija: ")
                saskaita.prideti(suma, siuntejas, info)
            case 2:
                suma = abs(float(input("Suma: ")))
                isigyta = input("Įsigyta prekė/paslauga: ")
                info = input("Papildoma informacija: ")
                saskaita.isimti(suma, isigyta, info)
            case 3:
                saskaita.parodyti_balansa()
            case 4:
                print(saskaita.zurnalas)
            case 0:
                break
