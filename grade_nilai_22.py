nama = input("masukan nama anda  : ")
nilai_harian = int(input("nilai harian = "))
nilai_uts = int(input("nilai UTS : "))
nilai_uas = int(input("nilai UAS : "))
nilai_akhir = (nilai_harian+nilai_uts+nilai_uas)/3

if nilai_akhir > 85 and 100:
    predikat ="amat baik"
elif nilai_akhir > 75 and 85:
    predikat = "baik"
elif nilai_akhir > 65 and 75:
    predikat = "cukup"
elif nilai_akhir > 55 and 65:
    predikat = "kurang"
else:
    predikat = "kurang sekali"
                    
print("nama anda : " , nama)
print("Nilai Harian : " , nilai_harian)
print("Nilai UTS : " , nilai_uts)
print("Nilai UAS : " , nilai_uas)
print("=======================")
print("Nilai akhir anda : " , nilai_akhir)
print("predikat anda : ", predikat)
                   
