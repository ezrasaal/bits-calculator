# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):
    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response > low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
for item in range(0, 2):
    integer = int_check("Integer: ", 1)
    print(integer)

print()

for item in range(0, 2):
        Width = int_check("Width: ", 1)
        print(Width)

print()
