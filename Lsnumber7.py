#Write a program that creates a list of 10 random integers. Then create two lists by
#name odd_list and even_list that have all odd and even values of the list respectively.

import random
odd_list = []
even_list = []
for values in range(10):
    results = random.randint(0, 50)
    if results % 2 == 0:
        even_list.append(results)
    else:
        odd_list.append(results)
print(f"{odd_list} and {even_list}")

