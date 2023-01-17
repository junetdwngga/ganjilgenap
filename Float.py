tugas = float(input("masukann nilai tugas :"))
uts = float(input("masukan uts : "))
uas = float(input("masukan nilai : "))

nilai = (0.15 + tugas ) + (0.35 * uts) + (0.59 * uas)

if nilai > 80:
    grade = "A"
elif nilai > 70:
    grade = "B"
elif nilai > 60:
    grade = "C"
elif nilai > 50:
    grade = "D"
else:
    grade = "E"

# menentukan status kelulusan berdasarkan nilai akhir
if nilai > 60:
    status = "lulus"
else:
    status = "tidak lulus"


#menampilkan nilai akhir,grade, dan status keluluhan
print("nilai akhir: %0.2f" % nilai)
print("grade: {}".format(grade))
print("status: {}".format(status))