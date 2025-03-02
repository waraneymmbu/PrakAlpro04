def validasi_input(pesan):
    try:
        nilai = int(input(pesan))
        if nilai > 0:
            return nilai
        else:
            print("Panjang sisi harus lebih dari 0.")
    except ValueError:
        print("Input tidak valid! Harap masukkan bilangan bulat positif.")

# Meminta input dari pengguna
sisi1 = validasi_input("Masukkan sisi 1: ")
sisi2 = validasi_input("Masukkan sisi 2: ")
sisi3 = validasi_input("Masukkan sisi 3: ")

# Menentukan jenis kesamaan sisi segitiga
if sisi1 == sisi2 == sisi3:
    print("3 sisi sama")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("2 sisi sama")
else:
    print("Tidak ada yang sama")
