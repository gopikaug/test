first=int(input("Enter the first year"))
last=int(input("Enter the last year"))
print("The leap years are")
for i in range(first,last):
    if(i%400==0 and i%100==0):
        print(i)
    if(i%4==0 and i%100!=0):
        print(i)
