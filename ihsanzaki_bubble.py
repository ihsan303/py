    
def sort_asc(array):
    n = len(array)
    for i in range(n):
        for j in range (n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

def sort_desc(array):
    n = len(array)
    for i in range(n):
        for j in range (n-i-1):
            if array [j] < array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

def garis():
    print("----------------------------------")

def rata_rata(angka):
    return sum(angka) / len(angka)

while True:
    garis()
    print("Masukan Tiga Buah Nilai:")
    angkaA = int(input("Nilai A : "))
    angkaB = int(input("Nilai B : "))
    angkaC = int(input("Nilai C : "))
    angka =[angkaA,angkaB,angkaC]

    garis()
    print()
    print("Hasil Akhir ---")
    print("Urutan Nilai ascending : ",(sort_asc(angka)))
    print("Urutan Nilai descending : ",(sort_desc(angka)))
    print("Nilai terbesar : ",max(angka))
    print("Nilai Terkecil : ",min(angka))
    print("Rata-rata Nilai : ",round(rata_rata(angka)))

    if input('Tekan y untuk mengulang? ')!='y':
        break

    

