# score = 300
# if score > 100:                         # lebih dari
#     print("score is super pass test")
# elif score == 100:                       # sama dengan
#     print("score pass test")
# else:                                    # kurang dari
#     print("failed")

# # contoh lain
# a = 50
# b = 10
# if a > b:
#     print("Hello, World!")

# lebih aplikatif
rho = 9778
v = 25
d = 1
miu = 12

reynold = (rho * v * d)/ miu
if reynold > 4000:
    print("turbulent")
elif reynold == 4000:
    ("transisi")
else:
    print("laminar")
