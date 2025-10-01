n = int(input("Enter a number:"))
print(n)
i=0
if n==0:
    print("Enter a number greater than Zero")
else:
 while True:
    i+=1
    if n == 1:
        break
    elif n % 2 == 0:
        n = n // 2
    elif n % 2 == 1:
        n = (3 * n) + 1
    else:
        print("NO way for this condition since a number can only be odd or even")
    print(n)
    
print("Number of iterations:",i)
