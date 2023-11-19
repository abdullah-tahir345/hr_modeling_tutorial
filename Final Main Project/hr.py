# --Policies
class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours

class SalaryPayroll(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        return self.weekly_salary

    
class HourlyPayroll(PayrollPolicy):
    def __init__(self, pay_per_hour):
        super().__init__()
        self.pay_per_hour = pay_per_hour
        
    def calculate_payroll(self):
        return self.hours_worked * self.pay_per_hour
    

class ComisssionPayroll(SalaryPayroll):
    def __init__(self, weekly_salary, comission):
        super().__init__(weekly_salary)
        self.comission = comission
    
    @property
    def comission_calculate(self):
        # Inheriting from base class SalaryPayroll and it's inheriting from PayrollPolicy
        sales = self.hours_worked / 5
        return sales * self.comission
    
    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        return fixed_salary + self.comission_calculate

class LTDPayroll:
    def __init__(self):
        self._base_policy = None

    def track_work(self, hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll()
        return base_salary * 0.6

    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError('Base policy missing')


class _PayrollSystem:
    def __init__(self):
        self._employee_policies = {
            1 : SalaryPayroll(3000),
            2 : SalaryPayroll(1500),
            3 : HourlyPayroll(100)
            }
    
    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            return ValueError('Invalid Value')
        return policy
    
    def calculate_payroll(self, employees):
        print('Calculate Payroll')
        print('-----------------')
        for employee in employees:
            print(f'Payroll for : {employee.id} - {employee.name}')
            print(f' -  Check amount : {employee.calculate_payroll()}')
            if employee.address:
                print(f' -  Address : {employee.address}')
            print()
            
# Policy classes implementation omitted

_payroll_system = _PayrollSystem()

def get_policy(employee_id):
    return _payroll_system.get_policy(employee_id)

def calculate_payroll(employees):
    _payroll_system.calculate_payroll(employees)


