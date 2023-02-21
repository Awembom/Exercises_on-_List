#Write a program that prints the maximum value of the second half of the list.

list = [3,4,5,6,8,8,54,9,2,1,6,7,8,6,5,47,3,1]
i = 0
a = list[int((len(list)) / 2)]
for values in list:
    if i > ((int(len(list))) / 2):
        if values > a:
            a = values
    i += 1
print(a)

