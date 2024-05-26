x=input("Enter a number or enter done to exit:")
if x=="done":
    print("No values entered")
else:
    largest=int(x) 
    smallest=int(x)
    while True:
        try:
            x=input("Enter a number or enter done to exit:")
            if x=="done":
               break
            if int(x)>largest:
               largest=int(x)
            if int(x)<smallest:
               smallest=int(x)
        except:
            print("Enter a valid number")
print("Maximum is %d" %largest)
print("Minimum is %d" %smallest)
