# Dedi Yanto
# 71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# Dictionary

'''
Hachiko adalah seorang ketua kelas, suatu hari gurunya yang sangat 
sibuk meminta bantuan hachiko untuk mencatat nilai siswa-siswa yang
tuntas dan tidak tuntas berdasarkan KKM(kriteria ketuntasan minimal)
yang diberikan oleh gurunya. Gurunya telah memberikan data-data
nilai siswa-siswanya kepada Hachiko. Hachiko juga sudah diberitahukan
KKM yang harus dicapai oleh siswa-siswanya. Pada saat itu Hachiko
sedang banyak kerjaan dan tugas, dan kemudian dia meminta bantuan
kepada temannya yang merupakan seoarang yang hoby dengan programming,
untuk dibuatkan sebuah program yang dapat membantu pekerjaannya.
Hachiko menuliskan permintaan programnya sebagai berikut:

1.Dapat menghitung ketuntasan siswa berdasarkan rata-rata nilai
  yang diperoleh, dengan KKM yang ditentukan oleh user.
2.Banyaknya nama siswa dan nilai yang ingin diinputkan
  di tentukan oleh user
3.Program dapat menampilkan nama siswa yang sudah 
  diinputkan sebelumnya, nilai rata-rata siswa tersebut,
  dan juga keterangan apakah siswa tersebut tuntas atau tidak.

Anggaplah anda adalah temannya hachiko, bantulah hachiko untuk
membuat program seperti diatas. Data nama siswa dan nilai yang 
diterima harus dimasukkan kedalam dictionary!!.
'''

'''

Input:
banyak siswa = 2
banyak nilai = 2
KKM = 78

Nama siswa : Toni
Nilai 1 = 70
Nilai 2 = 60

Nama siswa : ayu
Nilai 1 = 90
Nilai 2 = 70

Proses:
Key/kata kunci ke 1 = Toni
Value = [70,60]

Key/kata kunci ke 2 = Ayu
Value = [90,70]

Key : Toni
(70+60)/2 >= 78 ?

Key : Ayu
(90+70)/2 >= 78 ?

Ouput:
Nama : Toni
Nilai rata-rata : 65
Keterangan : Tidak Tuntas

Nama : Ayu
Nilai rata-rata: 80
Keterangan : Tuntas

'''

# Source Code
banyak_siswa = int(input("Masukkan Banyak Siswa : "))
nilai = int(input("Masukkan Banyak Nilai : "))
kkm = float(input("Masukkan KKM : "))

data = {}

for i in range(banyak_siswa):
  nama = input("\nMasukkan Nama Siswa : ")
  data.setdefault(nama,[])
  for j in range(nilai):
    hasil = float(input("Masukkan Nilai ke-"+str(j+1)+': '))
    data[nama].append(hasil)
print()

for i in data.keys():
  total = 0
  for j in data[i]:
    total += j
  rata2 = total/nilai
  if rata2 >= kkm:
    print('='*25)
    print('Nama :',i,'\nRata-rata Nilai :',round(rata2,2),'\nKeterangan : Tuntas !')
    print()
  else:
    print('='*25)
    print('Nama :',i,'\nRata-rata Nilai :',round(rata2,2),'\nKeterangan : Tidak Tuntas !')
    print()
