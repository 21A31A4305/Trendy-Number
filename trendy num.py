n=int(input())
if n>99 and n<=999:
    p=n//10
    q=p%10
    if q%3==0:
        print("it is a trendy number")

    else:
        print("it is not a trendy number")
else:
    print("Invalid input")