# This Excercise was pretty annoying..


# Giving Empty Values to both Largest & Smallest Variables

Largest = None
Smallest = None
while True:

    # Adding Try & Except to decline all Strings Except for "done", So if the Input == Done it will break the loop , otherwise it will transform the input
    # value into and integr so it will trigger the except condition if any other string is inputed

    try:
        num = input("Enter a Number: ")
        if num == 'done':
            break
        elif Largest is None:
            Largest = int(num)
            Smallest = int(num)
        elif int(num) > Largest:
            Largest = int(num)
        elif int(num) < Smallest:
            Smallest = int(num)
    except:
        print("Invalid input")

print('Maximum Is: ', Largest)
print('Minimum Is: ', Smallest)
