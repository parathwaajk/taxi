select=input("enter F OR C 0R K:")
select=select.upper()
d=int(input("enter the value:"))
if select=="F":
    k=d+273
    c=(5/9)*(d-32)
    print("celsius{0},kelvin{1}".format(c,k))
elif select=="c":
    f=1.8*d+32
    k=d+273
    print("farenhein{0},kelvin:{1}".format(f,k))
else:
    c=d+273
    f=1.8*d+32
    print("farenheit{0},celsius{1}".format(f,c))