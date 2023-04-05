class Employee:

    def __init__(self):

        self.name = input ("Masukan Nama : ")

        self.salary = int(input ("Nominal Gaji : "))

        self.grade = int(input ("Masukan Grade: "))

        self.num_children = int(input ("Jumlah Anak : "))

        self.married = input ("Menikah? (ya/tidak) :")

    def get_salary(self):

        # Hitung tunjangan golongan

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
        
        # Hitung tunjangan anak

        if self.num_children > 0:

            allowance_children = 0.02 * self.salary * self.num_children

        else:

            allowance_children = 0
        
        # Hitung tunjangan istri

        if self.married == "ya":

            allowance_spouse = 0.1 * self.salary

        else:

            allowance_spouse = 0
        
        # Hitung total gaji sebelum pajak

        total_salary = self.salary + allowance_grade + allowance_children + allowance_spouse

        # Hitung pajak

        if total_salary <= 5000000:

            tax = 0.05 * total_salary

        elif total_salary <= 10000000:

            tax = 0.1 * total_salary

        else:

            tax = 0.15 * total_salary

        # Hitung bonus

        if self.grade == 1 and self.num_children >= 3:

            bonus = 300000
        
        if self.grade == 2 and self.num_children >= 3:

            bonus = 400000
        
        elif self.grade == 3 and self.num_children >= 3:

            bonus = 500000

        else:

            bonus = 0

        # Hitung total gaji setelah pajak dan bonus

        totall = total_salary - tax + bonus  
    
        print ("\n","-"*50)
        print ("Tunjangan Golongan : ", allowance_grade)
        print ("Tunjangan Anak     : ", allowance_children)
        print ("Tunjangan Istri    : ", allowance_spouse)
        print ("Pajak              : ", tax)
        print ("Bonus              : ", bonus)
        print ("-"*40)
        print ("\nTotal Gaji         : ",totall)


a = Employee()
a.get_salary()
