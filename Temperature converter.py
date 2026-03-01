print("Temperature converter")
choice1=("faherenheit to celsics")
choice2=("celcius to fahrenheit")
choice=int(input("enter your choice"))
x=float(input("enter temperature value"))
if(choice==1):
    print("temp",(x-32)*(5/9))
elif(choice==2):
    print("temp",(x*(9/5)+32))
else:
    print("invalid choice")