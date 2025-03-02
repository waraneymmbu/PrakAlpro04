try:
    suhu = int(input("Masukkan suhu tubuh: "))
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except ValueError:
    print("Error: Input suhu harus berupa angka")



try:
    bilangan = int(input("Masukkan suatu bilangan: "))
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except ValueError:
    print("Error: Input harus berupa bilangan bulat")


try:
    a = int(input("Masukkan bilangan pertama: "))
    try:
        b = int(input("Masukkan bilangan kedua: "))
        try:
            c = int(input("Masukkan bilangan ketiga: "))
            if a > b and a > c:
                print("Terbesar:", a)
            elif b > a and b > c:
                print("Terbesar:", b)
            elif c > a and c > b:
                print("Terbesar:", c)
            else:
                print("Ada beberapa bilangan yang sama besar")
        except ValueError:
            print("Error: Input bilangan ketiga harus berupa angka")
    except ValueError:
        print("Error: Input bilangan kedua harus berupa angka")
except ValueError:
    print("Error: Input bilangan pertama harus berupa angka")

