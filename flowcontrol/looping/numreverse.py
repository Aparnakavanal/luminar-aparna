num=int(input("enter the number"))
while(num!=0):
    digit=num%10
    num=num//10
    print(digit,end="")