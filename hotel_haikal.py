def garis() :
    print("==========================")
   
while True:
    print("======= HOTEL SMK JAKARTA PUSAT 1")
    print("-- lama inap -- superior -- deluxe -- premium --")
    print("-- 1/2hari --200.000/day -- 150.000/day -- 100.000/day")

    tipe_kamar = input("masukkan tipe kamar :")
    lama_inap = int(input("masukkan lama inap :"))

    if tipe_kamar == "superior":
        if lama_inap <=2 :
            total_harga = 200000
        elif lama_inap <= 4 :
            total_harga = 400000
        else:
            total_harga = 600000

    elif tipe_kamar == "deluxe":
        if lama_inap <=2 :
            total_harga = 150000*lama_inap
        elif lama_inap <= 4 :
            total_harga = 150000*lama_inap
        else:
            total_harga = 150000*lama_inap

    elif tipe_kamar == "premium":
        if lama_inap <=2 :
            total_harga = 100000*lama_inap
        elif lama_inap <= 4 :
            total_harga = 100000*lama_inap
        else:
            total_harga = 100000*lama_inap      


    garis()
    print("Kamar yang dipilih : ",(tipe_kamar))
    print("lama inap : ",(lama_inap))
    print("Total Harga : ",(total_harga))

    if input('Mau pilih ulang? ') != 'y':
        break
