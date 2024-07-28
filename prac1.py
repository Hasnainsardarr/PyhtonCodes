sum=0
while(True):
    userinput = input("enter the ptice: \n")
    if(userinput!='q'):
        sum = sum+int(userinput)
        print(f"order total so far {sum}")

    else:
        print(f"thanks for using calcualtr your total bill is {sum} thanks for shoping ")

        break

