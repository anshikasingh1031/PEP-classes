class Employee:
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,emp_id,name,monthly_salary):
        super().__init__(emp_id,name)
        self._monthly_salary=monthly_salary

        #encapsulation beacuse salary is protected
    def calculate_salary(self):
        return self._monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self,emp_id,name,hour_worked,rate_per_hour):
        super().__init__(emp_id,name)
        self._hour_worked=hour_worked
        self._rate_per_hour=rate_per_hour
    def calculate_salary(self):
        return self._hour_worked*self._rate_per_hour
    
class payrollApp:
    def __init__(self):
        self.employee=None
    def create_employee(self,emp_type):
        if emp_type=="FullTime":
            self.employee=FullTimeEmployee(1,"amit",5000)
        else:
            self.employee = PartTimeEmployee(2, "Neha", 80, 500)
        return "Employee Created"
    def get_salary(self):
        return self.employee.calculate_salary()
    
app = payrollApp()
print(app.create_employee("FullTime"))
print("Salary:", app.get_salary())
app2 = payrollApp()
print(app2.create_employee("PartTime"))
print("Salary:", app2.get_salary())

            