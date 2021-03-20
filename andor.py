#check whether the given input is divisible by 2 andor 6
n = int(input("enter n:"))
if n%2 == 0 and n%6 == 0:
    print(n, "is divisible by both 2 and 6")
elif n%2 == 0 or n%6 ==0:
    print(n, "is either divisible by 2 or 6")
else:
    print(n, "is neither divisible by 2 nor 6")

