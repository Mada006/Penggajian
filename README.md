# APLIKASI PENGGAJIAN
Aplikasi penggajian ini adalah tugas dari mata kuliah OOP, dalam aplikasi ini user dapat melakukan perhitungan total gaji karyawan dengan mudah.

### Penjelasan Program
##### Pembuatan Class
class Employee memiliki beberapa variable/ object yang berisi data dari input user.
```sh
class Employee:

    def __init__(self, name, salary, grade, num_children, married):
        self.__name = name
        self.__salary = salary
        self.__grade = grade
        self.__num_children = num_children
        self.__married = married
```
Proses perhitungan gaji ada dalam fungsi get_salary ()
```sh
def get_salary(self):
```
Menghitung tunjangan golongan :
(tunjangan golongan = persenan sesuai grade * gaji pokok)
```sh
if self.__grade == 1:
            allowance_grade = 0.05 * self.__salary
        elif self.__grade == 2:
            allowance_grade = 0.1 * self.__salary
        elif self.__grade == 3:
            allowance_grade = 0.15 * self.__salary
        elif self.__grade == 4:
            allowance_grade = 0.2 * self.__salary
        else:
            allowance_grade = 0.2 * self.__salary
```
Menghitung tunjangan anak :
(tunjangan anak = 0.02 * gaji pokok * jumlah anak)
```sh
if self.__num_children > 0:
    allowance_children = 0.02 * self.__salary * self.__num_children
else:
    allowance_children = 0   
```
Menghitung tunjangan istri:
(tunjangan istri = 0.1 * gaji pokok)
```sh
if self.__married == "yes":
    allowance_spouse = 0.1 * self.__salary
else:
    allowance_spouse = 0 
```
Total gaji sebelum dipotong pajak:
```sh
total_salary = self.__salary + allowance_grade + allowance_children + allowance_spouse  
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
if self.__grade == 1 and self.__num_children >= 2:
    bonus = 500000
elif self.__grade == 2 and self.__num_children >= 2:
    bonus = 700000
elif self.__grade == 3 and self.__num_children >= 2:
    bonus = 1000000
elif self.__grade == 4 and self.__num_children >= 2:
    bonus = 1400000
else:
    bonus = 0
```
Total gaji setelah pajak dan bonus:
```sh
total_salaryy = f"Total Salary       : {int(total_salary - tax + bonus)}"
```
Menampilkan hasil :
```sh
print ("\n","="*30)
print(f"Employee Name      : {self.__name}")
print(f"Allowance Grade    : {int(allowance_grade)}")
        
if self.__married == "yes":
    print(f"Allowance Spouse   : {int(allowance_spouse)}")
    print(f"Allowance Children : {int(allowance_children)}")
        
print(f"Tax                : {int(tax)}")
print(f"Bonus              : {int(bonus)}")
        
       
return total_salaryy
```

Input :
```sh
loopp = "y"
while loopp == "y" :
    name_input         = input      ("Enter Name         : ")
    salary_input       = int (input ("Salary             : IDR "))
    grade_input        = int (input ("Grade              : "))
    status_input       = input      ("Married? (yes/no)  : ")
    if status_input == "yes" :
        children_input = int (input ("Number of Children : "))
    else :
        children_input = 0
    
    a = Employee (name_input, salary_input,grade_input,children_input, status_input)
    print (a.get_salary())

    loopp = input         ("\nNew Calculation? (y/n) : ")
```
