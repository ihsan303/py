def urutasc(mylist):
    for i in range(len(mylist)-1,0,-1):
        for j in  range (i):
            if mylist [j] > mylist[j+1]:
                simpan = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = simpan
    print(mylist)

def urutadsc(mylist):
    for i in range(len(mylist)-1,0,-1):
        for j in  range (i):
            if mylist [j] < mylist[j+1]:
                simpan = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = simpan
    print(mylist)

print("Program mengurutkan data dengan metode bubble sort")

angka1=int(input("masukan bilangan ke 1 : "))
angka2=int(input("masukan bilangan ke 2 : "))
angka3=int(input("masukan bilangan ke 3 : "))
angka4=int(input("masukan bilangan ke 4 : "))
angka5=int(input("masukan bilangan ke 5 : "))
angka6=int(input("masukan bilangan ke 6 : "))
angka7=int(input("masukan bilangan ke 7 : "))
angka8=int(input("masukan bilangan ke 8 : "))
angka9=int(input("masukan bilangan ke 9 : "))
angka10=int(input("masukan bilangan ke 10 : "))

angka=[angka1,angka2,angka3,angka4,angka5,angka6,angka7,angka8,angka9,angka10]

print("=============================")
print("Pilih metode pengurutan")
print("1. sorting ascending \n2. sorting descending")
pilih=input("metode yang diPilih : ")

print("=============================")
print("Data sebelum di urutkan : ")
print(angka)
print("Data setelah di urutkan : ")

if pilih==('1'):
    urutasc(angka)
else:
    urutdsc(angka)

home=input("Kembali ke Menu utama (Y/N) ? ")
text=print("Progam Menurut Data menggunakan metode bubble sort")
back=print("")
garis=("=============================")
if home==("Y"):
    garis
    text
    angka1=int(input("masukan bilangan ke 1 : "))
    angka2=int(input("masukan bilangan ke 2 : "))
    angka3=int(input("masukan bilangan ke 3 : "))
    angka4=int(input("masukan bilangan ke 4 : "))
    angka5=int(input("masukan bilangan ke 5 : "))
    angka6=int(input("masukan bilangan ke 6 : "))
    angka7=int(input("masukan bilangan ke 7 : "))
    angka8=int(input("masukan bilangan ke 8 : "))
    angka9=int(input("masukan bilangan ke 9 : "))
    angka10=int(input("masukan bilangan ke 10 : "))
    garis
    print("Pilih metode Pengurutan : ")
    print("1. Sorting Ascending /n2.Sorting Descending ")
    print=input("metode yang di pilih : ")
    garis
    print("Data sebelum di urutkan : ")
    print(angka)
    print("Data setelah di urutkan : ")
    if pilih==('1'):
        urutasc(angka)
    else:
        urutdsc(angka)
    home=input("kembali ke menu utama")
else:
    back
    

