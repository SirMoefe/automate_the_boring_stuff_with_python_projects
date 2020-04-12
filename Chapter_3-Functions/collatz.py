"""The Collatz Sequence"""


def collatz(number):
    count = 0
    while number != 1:
        if number % 2 == 0:
            count += 1
            number //= 2
            print(number)
        else:
            number = (number * 3) + 1
            count += 1
            print(number)
    print()
    print()
    print(50*"-")
    print("It took " + str(count) + " loops to solve it")
    print(50*"-")
    print()
    print()


try:
    my_number = input("Enter a number: ")
    collatz(int(my_number))

except(ValueError):
    print("You have to enter a number!")
except(KeyboardInterrupt):
    print("Program was interrupted by user and ends now. Bye bye...")
