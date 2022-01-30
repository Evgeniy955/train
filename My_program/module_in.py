def my_input(min_int, msg, ex_msg, logic_flageTrue):
    while True:
        try:
            res = int(input(msg))
            if logic_flageTrue:
                if res > min_int:
                    return res
            elif not logic_flageTrue:
                if res >= min_int:
                    return res
        except ValueError:
            print(ex_msg)

my_input(0, "Enter the number of coffee cups: ", "You are enter not a number.", True)