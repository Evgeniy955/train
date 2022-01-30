total = 0
while True:
    try:
        x = int(input("Please enter the number: "))
        if x > 0:
            break
    except ValueError:
        print('You are enter not a number.')

for i in range(x):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
