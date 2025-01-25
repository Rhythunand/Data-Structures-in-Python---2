my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3,)
print(my_tuple)

my_tuple = (1, "Hello", 2, 3)
print(my_tuple)

n_tuple = ("Mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])

print("Sliced : ", n_tuple[1:4])

for letter in (my_tuple) :
  print("Hello", letter)