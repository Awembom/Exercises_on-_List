#Write a function that prompts the user to enter five numbers, then invoke a function to find the GCD of these numbers.
def take_numbers():
    list = []
    for i in range(5):
        number = input("Enter the number: ")
        list.append(number)
    return list


