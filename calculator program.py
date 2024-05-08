print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter the chocie (1/2/3/4)")
if ( choice in ("1" ,"2" ,"3" ,"4")):
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    if(choice == "1"):
        print(num1,"+",num2,"=",num1+num2)
    elif(choice == "2"):
        print(num1,"-",num2,"=",num1-num2)
    elif(choice == "3"):
        print(num1,"*",num2,"=",num1*num2)
    else:
        print(num1,"/",num2,"=",num1/num2)

else:
    print("Invalid operation")
