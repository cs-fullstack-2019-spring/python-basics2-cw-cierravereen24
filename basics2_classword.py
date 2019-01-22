import random
def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()
# Problem1
# Create a random number. Print the number.
# Hint:
# import random
# randomNumber = random.randint(0,9)

# def problem1():
#     randomnumber = random.randint(0,10987)
#     print(randomnumber)
#
# if __name__ == '__main__':
#     main()

# problem2
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.

# def problem2():
#     while (True):
#         letter = input("Enter the letter of your first name: ")
#         if letter == "q":
#             break
#
# if __name__ == '__main__':
#     main()

# def problem3():
#     while (True):
#         number = int(input("Enter a positive number "))
#         for positive in range(number):
#             print(positive)
#         if number == 0:
#             break
#
# if __name__ == '__main__':
#     main()

Problem4
Create a function that creates a random number.
Ask the user to guess the random number.
Keep letting the user guess until they get it right, then quit.
If they don't get it right, tell them if their next guess has to be higher or lower.


def problem4():
    number = random.randint(0,10)
    while(True):
        prompt = int(input("Enter a number from 0 to 10: "))
        if number == prompt:
            print("You are correct!")
            break
        elif prompt > number:
            print("LOWER!")
        elif prompt < number:
            print("HIGHER!")

if __name__ == '__main__':
    main()
