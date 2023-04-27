class Employee:

    def __init__(self, name, salary, grade, num_children, married):
        self.__name = name
        self.__salary = salary
        self.__grade = grade
        self.__num_children = num_children
        self.__married = married

    def get_salary(self):
        # Hitung tunjangan golongan
        if self.__grade == 1:
            allowance_grade = 0.05 * self.__salary
        elif self.__grade == 2:
            allowance_grade = 0.1 * self.__salary
        else:
            allowance_grade = 0.15 * self.__salary

        # Hitung tunjangan anak
        if self.__num_children > 0:
            allowance_children = 0.02 * self.__salary * self.__num_children
        else:
            allowance_children = 0    

        # Hitung tunjangan istri
        if self.__married == "yes":
            allowance_spouse = 0.1 * self.__salary
        else:
            allowance_spouse = 0       

        # Hitung total gaji sebelum pajak
        total_salary = self.__salary + allowance_grade + allowance_children + allowance_spouse  

        # Hitung pajak
        if total_salary <= 5000000:
            tax = 0.05 * total_salary
        elif total_salary <= 10000000:
            tax = 0.1 * total_salary
        else:
            tax = 0.15 * total_salary    

        # Hitung bonus
        if self.__grade == 3 and self.__num_children >= 3:
            bonus = 500000
        else:
            bonus = 0
            
        # Hitung total gaji setelah pajak dan bonus
        total_salaryy = f"Total Salary       : {int(total_salary - tax + bonus)}"

        # HASIL
        print ("\n","="*30)
        print(f"Employee Name      : {self.__name}")
        print(f"Allowance Grade    : {int(allowance_grade)}")
        
        if self.__married == "yes":
            print(f"Allowance Spouse   : {int(allowance_spouse)}")
            print(f"Allowance Children : {int(allowance_children)}")
        
        print(f"Tax                : {int(tax)}")
        print(f"Bonus              : {int(bonus)}")
        
       
        return total_salaryy
    

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