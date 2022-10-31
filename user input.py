# username = input("Enter username: ")
# print("Username is: " + username) # hasil = Username is (input)

# contoh lain
# number = (input("enter number: "))
# print("Number input is: "+ number)

# contoh 2
# number = int(input("enter number: "))
# answer = int(number * 2) 
# print(answer) 

# lebih aplikatif (reynold int input)
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

# lebih aplikatif (reynold float input)
rho = float(input("Enter Rho Number: "))
v = float(input("Enter velocity Number: "))
d = float(input("Enter Diameter Number: "))
miu = float(input("Enter viscosity Number: "))
reynold = (rho * v * d)/miu
if reynold > 4000.0:
    print("turbulent")
elif reynold == 4000.0:
    print("transisi")
else:
    print("laminar")