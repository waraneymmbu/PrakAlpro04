bulan = int(input("Masukkan bulan (1-12): "))

hari_dalam_bulan = {
    1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

if bulan in hari_dalam_bulan:
    print(f"Jumlah hari: {hari_dalam_bulan[bulan]}")
else:
    print("Bulan yang diinputkan tidak valid.")
