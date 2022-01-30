while True:
    try:
        lines = int(input("Please enter the number of lines: "))
        if lines > 0:
            break
    except ValueError:
        print('You are not a whole number.')

x = [print("*" * i) for i in range(1, lines + 1)]
