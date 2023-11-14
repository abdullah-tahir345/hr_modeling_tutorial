# hr_modeling_tutorial

Employee Management System

This Python project is an Employee Management System that encompasses various aspects of employee information, roles, and productivity. The system is designed with an object-oriented approach, providing classes to represent employees, payroll systems, productivity tracking, and more.

<h4>Key Components</h4>
<b>contacts.py</b>
<li>Defines the Address class to represent employee addresses.</li>
<li>Implements an AddressBook to manage employee addresses.</li>
<b>employees.py</b>
<li>Introduces the Employee class, representing individual employees with attributes such as ID, name, address, role, and payroll.</li>
<li>The class hierarchy includes roles like Manager, Secretary, SalesBoy, FactoryPerson, and TemporarySecretary.</li>
<li>The EmployeeDatabase class manages a list of employees, their roles, and addresses.</li>
<b>hr.py</b>

<li>Implements the PayrollSystem class, managing various payroll policies for different employees.</li>
<li>Defines payroll policies such as SalaryPayroll, HourlyPayroll, and ComisssionPayroll.</li>
<b>productivity.py</b>

<li>Introduces role-specific productivity classes (ManagerRole, SecretaryRole, SalesRole, FactoryPersonRole) to simulate employee duties.</li>
<li>The ProductivitySystem class manages roles and simulates employee productivity.</li>
<b>program.py</b>

<li>The main program instantiates objects for courses, instructors, students, and the online learning platform.</li>
<li>Display information about the objects and how objects instentiated and employees objects pass to the payroll system and 
  productivity system</li>
<h4>Additional Features</h4>
<li>Employee addresses are managed through an AddressBook.</li>
<li>The project simulates various roles and their specific duties using the productivity system.</li>
<li>Payroll calculations are handled through different policies based on employee roles.</li>
