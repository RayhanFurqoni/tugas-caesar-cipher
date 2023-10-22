abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(kalimat,cipher_key):
  kalimat = kalimat.lower()
  hasil_encode = ''
  for karakter in kalimat:
    if karakter in abjad:
      index_lama = abjad.index(karakter)
      index_baru = (index_lama + cipher_key ) % len(abjad)
      abjad_baru = abjad[index_baru]
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode

while True:
    print("Pilih operasi:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == '1':
        kalimat = input('Masukkan kalimat yang ingin dienkripsi: ')
        key = int(input('Masukkan cipher key: '))
        kalimat_hasil = encode(kalimat, key)
        print('Hasil enkripsi kalimat adalah:', kalimat_hasil)
    elif pilihan == '2':
        kalimat = input('Masukkan kalimat yang ingin didekripsi: ')
        key = int(input('Masukkan cipher key: '))
        kalimat_awal = encode(kalimat, -key)
        print('Hasil dekripsi kalimat adalah:', kalimat_awal)
    elif pilihan == '3':
        break
    else:
        print("Masukkan pilihan yang benar!")
