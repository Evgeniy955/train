while True:
    try:
        x = int(input("Please enter the number: "))
        if x > 0:
            break
    except ValueError:
        print('You are enter not a number.')

y = [print(i, "Is EVEN") if i % 2 == 0 else print(i, "Is ODD") for i in range(x)]
