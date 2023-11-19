from productivity import get_role
from hr import get_policy
from contacts import get_employee_address
from representations import AsDictionaryMixin

class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {
                'name' : 'James',
                'role' : 'manager'
                },
            2: {
                'name' : 'Norie',
                'role' : 'secretary'
                },
            3: {
                'name' : 'Barbie',
                'role' : 'factory'
                }
            }
        #self.productivity = ProductivitySystem()
        #self.payroll = PayrollSystem()
        #self.employee_address = AddressBook()
    
    @property
    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError(employee_id)
        return info
    
    #def _create_employee(self, id, name, role):
    #   address = self.employee_address.get_employee_address(id)
    #   employee_role = self.productivity.get_role(role)
    #   payroll_policy = self.payroll.get_policy(id)
    #   return Employee(id, name, address, employee_role, payroll_policy)
    

class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get('name')
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get('role'))
        self._payroll = get_policy(self.id)

        
    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()
    
    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy

employee_database = _EmployeeDatabase()

# class Manager(Employee, ManagerRole, SalaryPayroll):
#     def __init__(self, id, name, weekly_salary):
#         # MRO
#         SalaryPayroll.__init__(self, weekly_salary)
#         super().__init__(id, name)

# class Secretary(Employee, SecretaryRole, SalaryPayroll):
#     def __init__(self, id, name,weekly_salary):
#         # MRO
#         SalaryPayroll.__init__(self, weekly_salary)
#         super().__init__(id, name)
        
# class SalesBoy(Employee, SalesRole, ComisssionPayroll):
#     def __init__(self, id, name, weekly_salary, comission):
#         # MRO
#         ComisssionPayroll.__init__(self, weekly_salary, comission)
#         super().__init__(id, name)
        
# class FactoryPerson(Employee, FactoryPersonRole, HourlyPayroll):
#     def __init__(self, id, name, work_hours, pay_per_hour):
#         HourlyPayroll.__init__(self, work_hours, pay_per_hour)
#         super().__init__(id, name)

# #Multiple Inheritance
# class TemporarySecretary(Employee, SecretaryRole, HourlyPayroll): #--Warning shows because HourlyPayroll and SecretaryRole is inherited from staric(*)
#     def __init__(self, id, name, work_hours, pay_per_hour):
#         HourlyPayroll.__init__(self, work_hours, pay_per_hour)
#         super().__init__(id, name)
        
        
        
        
        
