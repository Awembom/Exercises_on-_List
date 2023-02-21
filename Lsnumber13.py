#Write a program that creates a list of numbers 1–100 that are either divisible by
#5 or 6.

list = []
for numbers in range(1,101):
    if ((numbers) % 5) == 0 or ((numbers) % 6) == 0:
        list.append(numbers)
print(list)