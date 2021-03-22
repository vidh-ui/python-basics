nos=(1,8,3,4,5,6,7)
print(nos)
print(nos[3])

if 2 in nos:
    print("2 is present")
else:
    print("2 not present")

sum=sum(nos)
ascending=sorted(nos)
#descending=tuple(reversed(nos))
size=len(nos)

print("sum=", sum)
print("ascending order", ascending)
#print("descending order", descending)
print("size=", size)

sq=tuple(x**2 for x in nos if x%2==0)
print(sq)