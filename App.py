import datetime as DateTime
from CustomDate import get_month_name_id, get_day_name_id


name = input("Masukkan nama anda: ")
address = input("Masukkan alamat rumah anda: ")

dateBirth = int(input("Masukkan tanggal lahir: "))
if dateBirth > 31:
    raise TypeError("Tanggal lahir tidak boleh lebih dari 31")
monthBirth = int(input("Masukkan bulan lahir: "))
if monthBirth > 12:
    raise TypeError("Bulan lahir tidak boleh lebih dari 12")
yearBirth = int(input("Masukkan tahun lahir: "))

dateParsed = DateTime.date(yearBirth, monthBirth, dateBirth)

print("========== BIODATA ==========\n")
print("Nama: ", name)
print("Alamat: ", address)
print("Tanggal lahir: ", get_day_name_id(dateParsed.strftime("%a")) + ",",
      dateParsed.strftime("%d"), get_month_name_id(dateParsed.strftime("%b")),
      dateParsed.strftime("%Y"))
