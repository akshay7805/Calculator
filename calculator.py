a=float(input("Enter the number: "))
b=float(input("Enter the number: " ))
c=input("Enter the symbol +,-,*,/ :  ")
match c:
    case "+":
        print("addition is :",a+b)
    case "-":
        print("subtraction is :", a-b)
    case "*":
        print("multiplication is :", a*b)
    case "/":
        print("divison is :", a/b)
    case _ :
        print("Enter the valid symbol to perform the operation")  