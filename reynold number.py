# reynold int input
rho = int(input("Enter Rho Number: "))
v = int(input("Enter velocity Number: "))
d = int(input("Enter Diameter Number: "))
miu = int(input("Enter viscosity Number: "))
reynold = (rho * v * d)/miu
if reynold > 4000:
    print("turbulent")
elif reynold == 4000:
    print("transisi")
else:
    print("laminar")


# reynold float input
rho = float(input("Enter Rho Number: "))
v = float(input("Enter velocity Number: "))
d = float(input("Enter Diameter Number: "))
miu = float(input("Enter viscosity Number: "))
reynold = (rho * v * d)/miu
print (reynold)
if reynold > 3999.0:
    print("turbulent")
elif reynold == 3999.0:
    print("transisi")
else:
    print("laminar")