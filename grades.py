#100-s, >90 A, >80 B, >70 C, >60 D, >50 E, <50 F
n= int(input("enter the mark"))
if n>100 or n<0:
    print("invalid marks")
elif n == 100:
    print("s grade")
elif n>90:
    print("A grade")
elif n>80:
    print("B grade")
elif n>70:
    print("C grade")
elif n>60:
    print("D grade")
elif n>50:
    print("E grade")
else:
    prinnt("Fail")