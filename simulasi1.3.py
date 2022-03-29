def garis():
    print("=====================")

print("====hotel Jakarat Pusat 1 ====")
print("---lama inap --- superior --- deluxe --- premium ---")
print("--1/2hari -- 200.000 -- 150.000 -- 100.000 --")
garis()


tipe_kamar = input("masukan tipe kamar : ")
lama_inap = int(input("waktu inap : "))


if tipe_kamar =="superior":
    if lama_inap <= 2 :
        total_harga = 200000
    elif lama_inap <= 4 :
        total_harga = 400000
    else:
        total_harga = 200000*lama_inap

elif tipe_kamar =="deluxe":
    if lama_inap <= 2 :
        total_harga = 150000
    elif lama_inap <= 4 :
        total_harga = 300000
    else:
        total_harga = 150000*lama_inap

elif tipe_kamar =="premium":
    if lama_inap <= 2 :
        total_harga = 100000
    elif lama_inap <= 4 :
        total_harga = 200000
    else:
        total_harga = 100000*lama_inap

garis()
print("tipe kamar : ",(tipe_kamar))
print("lama menginap : ",(lama_inap))
print("total harga : ", (total_harga))

tombol = input(" kemabali ke menu utama ? (Y/N)")
if tombol == "Y":
    tipe_kamar = input("Mausukan tipe kamar")
    lama_inap = int(input("Masukan lama inap"))


    if tipe_kamar == "superior":
        if lama_inap <= 2 :
            total_harga = 200000
        elif lama_inap <= 4 :
            total_harga = 200000*lama_inap
        else:
            total_harga = 200000*lama_inap

    elif tipe_kamar == "deluxe":
        if lama_inap <=2 :
            total_harga = 150000
        elif lama_inap <= 4 :
            total_harga = 150000*lama_inap
        else:
            total_harga = 150000*lama_inap

    elif tipe_kamar == "premium":
        if lama_inap <= 2 :
            total_harga = 100000
        elif lama_inap <= 4 :
            total_harga = 100000*lama_inap
        else:
            total_harga = 100000*lama-inap


    garis()
    print ("kamar yang di pilih : ", (tipe_kamar))
    print("wakti menginap : ", (lama_inap))
    print("total Harga : ", (total_harga))
else:
    print("Trimakasih telah menggunakan Hotel Kami")


        
