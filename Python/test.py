import random

b = random.randint(1, 10)
a = input("угадай чилсо от 1 до 10")

if a == b :
    print("Вы угадали")
else :
    print("Вы не угадали")