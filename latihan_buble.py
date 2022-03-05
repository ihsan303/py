#buat garis
def garis():
    print("........................")

#fungsi buble ascending(dari kecil ke basar)

def sort_asc(array):
    n = len(array) #n jumlah baris
    #perulang pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #bandingan elemen ke kanan
            if array[j] > array[j+1]:
                #jika lebih besar maka die pindah, berpindah
                array[j], array[j+1] = array[j+1], array [j]
    return array

#fungsi buble discending (dari besar ke kecil)
def sort_desc(array):
    n = len(array)  #n jumlah baris
    #peerulangan pertama
    for i in range (n):
        #perulangan kedua
        for j in range (n-i-1):
            #perbandingna elemen ke kanan
            if array[j] < array[j+i]:
                #jika lebih kecil makadie pindah, berpindah(swap)
                array[j], array[j+i] = array[j+i], array[j]
    return array

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka) / len(angka)

#input memasukan nilai
garis()
print("masukan nilai sebanyak yang kamu mau!")
angka = list(map(int, input("masukan nilainya : ").split()))
garis()
print()

#input memilih pilihan asc dan desc
garis()
print("pilh Metodo : ")
print("ascending = 1 | descending = 2")
pilih = int(input("pilih ="))
garis()

#menentukan nilai
if pilih == 1:
    print()
    print("HASIL AKHIR ----")
    print("Urutkan angka ascending :",(sort_asc(angka)))
else:
    print()
    print("HASIL AKHIR ----")
    print("Urutkan angka descending :",(sort_desc(angka)))

#cari angka terbesar
print("angka terbesar : ",max(angka))

#cari angka terkecil
print("angka terkecil : ",min(angka))

#jumlahkan angkanya
print("jumlah : ",sum(angka))

#tampilan rata rata
print("rata - rata : ",round(rata_rata(angka),2))
        
