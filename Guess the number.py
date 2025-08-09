number = int(input("Enter a number between 1 and 10: "))
tries = 6



while number != 1   and tries > 0:
    print("Wrong number, try again.")
    print("you have", tries, "tries left.")
    number = int(input("Enter a number between 1 and 10: "))
    tries -= 1
if tries == 0:
    print("Sorry, you are out of tries. The correct number was 1.")

if number == 1:
    print("You guessed the correct number!")