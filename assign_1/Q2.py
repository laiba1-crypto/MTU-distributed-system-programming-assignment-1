from abc import ABC, abstractmethod

# Define IValue interface
class I_Value(ABC):
    @abstractmethod
    def check_value(self):
        pass

# Base Value class
class Value(I_Value):
    def __init__(self, value):
        self._value = value

    def check_value(self):
        return self._value
# Add decorator class
class Addition(I_Value):
    def __init__(self, value, operand):
        self._value = value
        self._operand = operand

    def check_value(self):
        return self._value.check_value() + self._operand

# Sub decorator class
class Subtraction(I_Value):
    def __init__(self, value, operand):
        self._value = value
        self._operand = operand

    def check_value(self):
        return self._value.check_value() - self._operand
# Create a Value object with an initial value of 50
initial_value = Value(50)

# Create add decorator to add 20 to the initial value
addition_decorator = Addition(initial_value, 20)

# Create subtract decorator to minus 5 from previous value
subtraction_decorator = Subtraction(addition_decorator, 5)

# Get the final outcome
output = subtraction_decorator.check_value()

print(f"The output of the use case diagram is '{output}' ")  # Output: 65
