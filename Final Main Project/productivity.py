#Productivity System -- Roles
class ManagerRole:
    def perform_duties(self, hours):
        return f'yells for {hours} hours.'
    
class SecretaryRole:
    def perform_duties(self, hours):
        return f'do paper work for {hours} hours.'
    
class SalesRole:
    def perform_duties(self, hours):
        return f'take orders for {hours} hours on phone.'
    
class FactoryPersonRole:
    def perform_duties(self, hours):
        return f'make products for {hours} hours.'
    
    
    
    
    
class _ProductivitySystem:
    def __init__(self):
        self._roles = {
            'manager' : ManagerRole,
            'secretary' : SecretaryRole,
            'sales' : SalesRole,
            'factory' : FactoryPersonRole
            }
    
    def get_role(self, role_key):
        role_type = self._roles.get(role_key)
        if not role_type:
            raise ValueError('Invalid Role')
        return role_type()
        
    def track_system(self, employees, hours):
        print('Tracking Productivity Of Employee')
        print('---------------------')
        for employee in employees:
            print(employee.work(hours))
        print('')

# Role classes implementation omitted

_productivity_system = _ProductivitySystem()

def get_role(role_id):
    return _productivity_system.get_role(role_id)

def track(employees, hours):
    _productivity_system.track_system(employees, hours)

#productivitysystem = ProductivitySystem()
#print(productivitysystem.get_role('manager').perform_duties(40))