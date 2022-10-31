# # Ini merupakan contoh penggunaan tuple
# mytuple = ("ayam", "kucing", "babi")
# print(mytuple)
# print(len(mytuple)) # menunjukan jumlah data dalam tuple

# mytuple2 = ("singa")
# print(type(mytuple2)) # menunjukan bahwa hanya data string



# CONTOH OPERASI

tuple1 = ("anjing", "monyet", "semut")
tuple2 = (2, 5, 7, 12, 3)
tuple3 = (True, False, False)

# print(type(tuple1))
# print(type(tuple2))   #menunjukan ini kelas tuple
# print(type(tuple3))

# print(tuple1[0]) # menunjukan isi data tuple pada urut ke 0 untuk data pertama
# print(tuple2[-1]) # menunjukan isi data mulai dari belakang
# print(tuple2[2 : 4]) # menunjukan isi data ke 2 sampai sebelum data ke 4
# print(tuple2[:3]) # menunjukan isi data ke 0 sampai sebelum data ke 3
# print(tuple2[2:]) # menunjukan isi data ke 2 sampai selesai

# if "monyet" in tuple1:
#     print("ya ada monyet dalam tuple ini")

# if "monyet" in tuple2:
#     print("ya ada monyet dalam tuple ini") #mengetahui apa ada data tersebut
# else:
#     print("gaada monyet dalam tuple ini")

y = list(tuple1)  # mengganti isi tuple ke 1
y[1] = "sapi"
newtuple = tuple(y)
print(newtuple)

y = list(tuple1)  # menambah data isi tuple 
y .append("sapi")
newtuple2 = tuple(y)
print(newtuple2)

y = list(tuple1)  # menambah data isi tuple di bagian belakang
y = ("banteng",)
tuple1 += y
print(tuple1)

y = list(tuple1)  # menghapus data isi tuple tertentu
y .remove("monyet")
tuple10 = tuple(y)
print(tuple10)

del tuple1    # menghapus semua data tuple1
print(tuple1)