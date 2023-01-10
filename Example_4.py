'''
Python Docstrings
Python documentation strings (or docstrings) provide a convenient way of associating documentation
with Python modules, functions, classes, and methods.
It’s specified in source code that is used, like a comment, to document a specific segment of code.
Unlike conventional source code comments, the docstring should describe what the function does, not how.
'''


class Employee:
    """
    This is the class defined for Employee.
    """
    name = ""
    desig = ""

    def __init__(self, name, desig):
        """
            parameterized constructor in order to accept name and desig
        """
        self.name = name
        self.desig = desig

    def getname(self):
        """
        getter method to get the name
        """
        return self.name

    def getdesig(self):
        """
        getter method to get the designation
        """
        return self.desig


e1 = Employee("Sagar", "officer")
print(e1.getname())
print(e1.getdesig())

print(e1.__dict__)
print(Employee.__doc__)
print(e1.getname.__doc__)
print(e1.getdesig.__doc__)
print(e1.__init__.__doc__)
