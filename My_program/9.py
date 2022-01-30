while True:
    try:
        cofee = int(input("Enter the number of coffee cups: "))
        if cofee > 0:
            break
    except ValueError:
        print('You are enter not a number.')

bonus = cofee // 6

print(f"You have {bonus} free cups of coffee.")
