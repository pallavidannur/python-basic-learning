n = int(input("Enter the number you want to check: "))
f1 = 0
f2 = 1
if n == 0 or n == 1:
    print("Given number is a Fibonacci number.")
else:
    f3 = f1 + f2
    while f3 < n:
        f1 = f2
        f2 = f3
        f3 = f1 + f2
    if f3 == n:
        print("Given number is a Fibonacci number.")
    else:
        print("No, it is not a Fibonacci number.")


