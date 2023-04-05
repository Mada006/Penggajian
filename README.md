# APLIKASI PENGGAJIAN
Aplikasi penggajian ini adalah tugas dari mata kuliah OOP, dalam aplikasi ini user dapat melakukan perhitungan total gaji karyawan dengan mudah.

### Penjelasan Program
Pembuatan Class
```sh
class Employee:
```
Fungsi input() dipanggil dalam def _ _ init _ _(self):
```sh
def __init__(self):

        self.name = input ("Masukan Nama : ")

        self.salary = int(input ("Nominal Gaji : "))

        self.grade = int(input ("Masukan Grade: "))

        self.num_children = int(input ("Jumlah Anak : "))

        self.married = input ("Menikah? (ya/tidak) :")
```
Perhitungan gaji ada dalam fungsi get_salary ()
```sh
def get_salary(self):
```
Menghitung tunjangan golongan :
(tunjangan golongan = persenan sesuai grade * gaji pokok)
```sh
if self.grade == 1:
    allowance_grade = 0.05 * self.salary

elif self.grade == 2:
    allowance_grade = 0.1 * self.salary

elif self.grade == 3:
    allowance_grade = 0.15 * self.salary

elif self.grade == 4:
    allowance_grade = 0.2 * self.salary

else:
    allowance_grade = 0.15 * self.salary
```
Menghitung tunjangan anak :
(tunjangan anak = 0.02 * gaji pokok * jumlah anak)
```sh
if self.num_children > 0:
    allowance_children = 0.02 * self.salary * self.num_children

else:
    allowance_children = 0
```
Menghitung tunjangan istri:
(tunjangan istri = 0.1 * gaji pokok)
```sh
if self.married == "ya":
    allowance_spouse = 0.1 * self.salary

else:
    allowance_spouse = 0
```
Total gaji sebelum dipotong pajak:
```sh
total_salary = self.salary + allowance_grade + allowance_children + allowance_spouse
```
Menghitung pajak:
```sh
if total_salary <= 5000000:
    tax = 0.05 * total_salary

elif total_salary <= 10000000:
    tax = 0.1 * total_salary

else:
    tax = 0.15 * total_salary
```
Hitung bonus (bonus tidak dipotong pajak) :
```sh
if self.grade == 1 and self.num_children >= 3:
        bonus = 300000
 
if self.grade == 2 and self.num_children >= 3:
        bonus = 400000
        
elif self.grade == 3 and self.num_children >= 3:
        bonus = 500000

else:
        bonus = 0
```
Total gaji setelah pajak dan bonus:
```sh
totall = total_salary - tax + bonus 
```
Memanggil kelas dan fungsi:
```sh
a = Employee()
a.get_salary()
```
