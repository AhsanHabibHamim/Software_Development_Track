"""
Making a simple calculator using the methods atribute in class which can add, subtract, multiply and divide 2 numbers
"""

class Calculator:
    brand = 'Calculator Model: Casio MS 99'

    def add(self, num1, num2):
        result=f'The addition is {num1+num2}'
        return result
    
    def sub(self, num1, num2):
        result=f'The summetion is {num1-num2}'
        return result
    
    def mult(self, num1, num2):
        result=f'The Multiplication is {num1*num2}'
        return result
    
    def divide(self, num1, num2):
        result=f'The dividation is {num1/num2}'
        return result
    
My_Calculator=Calculator()
Add=My_Calculator.add(10,20)
Sub=My_Calculator.sub(100,20)
Mul=My_Calculator.mult(10,20)
Div=My_Calculator.divide(100,20)
print(My_Calculator.brand)
print(Add)
print(Sub)
print(Mul)
print(Div)

"""
Output:
Calculator Model: Casio MS 99
The addition is 30
The summetion is 80
The Multiplication is 200
The dividation is 5.0
"""