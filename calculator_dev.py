a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
op=input("enter the op value:")
if(op=="+"):
    print(a+b)
elif(op=="-"):
    print(a-b)
elif(op=="*"):
    print(a*b)
elif(op=="/"):
    if(b==0):
        print("b is cannot be zero")
    else:
        print(a/b)
elif(op=="//"):
    print(a//b)
elif(op=="%"):
    print(a%b)
elif(op=="**"):
    print(a**b)
else:
    print("enter valid op")