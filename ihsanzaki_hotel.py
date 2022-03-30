
def garis1():
    print("===================================")
def garis2():
    print("+----------------------------------------------------------------------------+")

while True:
    garis1()
    print(" HOTEL SUKASTRIO  ")
    print("Jln.sudirman raya no.30")
    garis2()
    print("| lama menginap      | Superior         | Deluxe          | Premium          |")
    garis2()
    print("|   1-2  hari        | 100.000/night    | 150.000/nigth   | 200.000/nigth    |")
    garis2()
    print("|   3-4  hari        | 90.000/night     | 135.000/nigth   | 180.000/nigth    |")
    garis2()
    print("|   1-2  hari        | 80.000/night     | 120.000/nigth   | 160.000/nigth    |")
    garis2()
    print("Tipe Kamar")
    print("1.Superior")
    print("2.Deluxe")
    print("3.Premium")
    tipe_kamar = input("Pilih Tipe Kamar  :")
    lama_inap = int(input("Lama Menginap     :"))

    if tipe_kamar =='1':
        if lama_inap <=2 :
            total_harga = 100000
        elif lama_inap <= 4 :
            total_harga = 90000
        else:
            total_harga = 80000*lama_inap
    elif tipe_kamar =='2':
        if lama_inap <=2 :
            total_harga = 150000
        elif lama_inap <= 4 :
            total_harga = 135000
        else:
            total_harga = 120000*lama_inap
    elif tipe_kamar =='3':
        if lama_inap <=2 :
            total_harga = 200000
        elif lama_inap <= 4 :
            total_harga = 180000
        else:
            total_harga = 160000*lama_inap
    
    print("Total Harga : ",(total_harga))
    if input('Ingin Memesan Lagi? (Y/N)  :') != 'y':
        break
            
    
