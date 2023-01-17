nilai = int(input("Masukan nilai Kamu :"))

if nilai >= 80 and nilai <= 100:
    print("A")
elif nilai >= 70 and nilai < 90:
    print("B")
elif nilai >= 60 and nilai < 70:
    print("C")
elif nilai >= 50 and nilai < 60:
    print("D")
elif nilai < 50 :
    print("E")
else:
    print('MASUKIN NILAINYA YANG BENER SAYANG')