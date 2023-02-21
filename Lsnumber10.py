# Make a list of the first eight letters of the alphabet, then using the slice operation
# do the following operations:
# a. Print the first three letters of the alphabet.
# b. Print any three letters from the middle.
# c. Print the letters from any particular index to the end of the list.

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(list[:3:])
print(list[3:6:])
print(list[2::])
