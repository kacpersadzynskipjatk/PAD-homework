import numpy as np


# Zad 1
def check_range(x, y, z):
    if y <= x <= z:
        print("x jest między y a z")
    else:
        print("x NIE jest między y a z")


check_range(4, 0, 20)
check_range(30, 0, 20)
check_range(-1, 0, 20)
check_range(20, 0, 20)


# Zad2
def unique_list(li):
    new_list = set(li)
    return new_list


my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]
u = unique_list(my_list)
print(u)

# Alternative
my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]
my_list = np.array(my_list)
print(np.unique(my_list))


# Zad3
def volume_of_sphere(r):
    print(round(4 / 3 * 3.14 * r ** 3, 2))


volume_of_sphere(2)
volume_of_sphere(1)
volume_of_sphere(10)
volume_of_sphere(17)


# Zad4
def num_fact(n):
    if n == 0:
        return 1
    else:
        return num_fact(n - 1) * n


print(num_fact(0))
print(num_fact(1))
print(num_fact(2))
print(num_fact(3))
print(num_fact(4))
print(num_fact(5))
print(num_fact(6))
