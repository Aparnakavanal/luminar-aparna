limit=int(input("enter the limit"))
i=1
ototal=0
etotal=0
while(i<=limit):
    if i%2==0:
        etotal+=i
    else:
        ototal+=i
    i=i+1
print(etotal)
print(ototal)

