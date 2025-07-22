print("hallo guys")
print("ketik nama kamu")
nama = input("siapa namamu? ")
print("halo", nama)
print("gimana", nama, "?")
umur = 10
print("kamu", 10, "tahun")

a=10
b=10
print("hasil penjumlahan a dan b adalah", a + b)
print("hasil pengurangan a dan b adalah", a - b)

while True:
    nilai_input = input("Masukkan nilai (angka): ")
    if nilai_input.isdigit():
        nilai = int(nilai_input)
        break
    else:
        print("Masukkan angka yang valid!")

if nilai >= 10:
    lulus = "lulus"
    for i in range(1):
        print("kamu hebat")
        print("kamu berhasil")
        print("Selamat ya!!")
else:
    lulus = "tidak lulus"
    for i in range(1):
        print("sayang banget ya ga berhasil")
        print("jangan menyerah")
        print("coba lagi ya")
