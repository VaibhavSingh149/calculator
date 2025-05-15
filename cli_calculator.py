class Calculator():
    @staticmethod
    def summ(*numbers):
        total = 0
        for nums in numbers:
            total += nums    
        return total
    @staticmethod
    def substract(*numbers):
        total = 0
        for nums in numbers:
            total += nums
        return total #given I am giving negativer numbers
    @staticmethod
    def divi(a,b):
        if b == 0:
            return "cannot divide by zero"
        return a/b
    @staticmethod
    def multi(*numbers):
        product = 1
        for a in numbers:
            product *=a
        return product
    #user gives input

while(True):
    try:
        ask = input("Enter operator:")
        if(ask == "Q"):
            break
        if(ask == "-"):
            args = map(int, input("Enter a number :").split())
            print("The ans will be", Calculator.substract(*args))
        elif(ask == "+"):
            args = map(int, input("Enter numbers: ").split())
            print("The ans will be", Calculator.summ(*args))
        elif(ask == "*"):
            args = map(int, input("Enter numbers: ").split())
            print("The ans will be", Calculator.multi(*args))
        elif(ask == "/"):
            a = int(input("Enter first number: "))
            b = int(input("Enter Second number: "))
            print("the ans wil be", Calculator.divi(a,b))
        else:
            print("Invalid Operator, choose from (+, -, *, /)")
    except ValueError:
        print("Invalid input, please enter numeric value")
    except Exception as e:
        print("Unexpected error occured",e)
