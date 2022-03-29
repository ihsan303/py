nama = input("\nNama : ")
nharian = float(input("Nilai Harian : "))
nuts = float(input("Nilai UTS : "))
nuas = float(input("Nilai UAS : "))

harian = nharian *30 / 100
uts = nuts * 30 / 100
uas = nuas * 30 / 100

nilai_akhir = harian + uts + uas

print("\n Nama : %s"%nama)
print("Nilai Harian : %d" %nharian)
print("Nilai UTS : %d" %nuts)
print("Nilai UAS : %d" %nuas)
print("Rata-rata : ",float(nilai_akhir))

if nilai_akhir >= 80:
    print("Predikat : A")
elif nilai_akhir >=70:
    print("Predikat : B")
elif nilai_akhir >=60:
    print("Predikat : C")
elif nilai_akhir >=50:
    print("Predikat : D")
elif nilai_akhir <=50:
    print("Predikat : E")
