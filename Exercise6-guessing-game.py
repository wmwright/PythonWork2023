while True:
    guess = int(input("When was Python 1.0 released? "))

    if guess == 1994:
        print("Correct!")
        break
    elif guess > 1994:
        print("It was earlier than that!")
    else:
        print("It was later than that!")
