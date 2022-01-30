def animal(animal_naming):
    while True:
        try:
            x = int(input(f"Enter the number of {animal_naming}: "))
            if x < 0:
                continue
            return x
        except ValueError:
            print('You are enter not a number.')


chickens = animal('Chickens')
pigs = animal('Pigs')
cows = animal('Cows')

sum_legs = chickens * 2 + cows * 4 + pigs * 4
print(f"Animals have {sum_legs} legs")
