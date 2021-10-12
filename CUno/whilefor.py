largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break

    try:
        pru = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None:
        largest = pru
        smallest = pru

    if largest < pru:
        largest = pru
    elif smallest > pru:
        smallest = pru

print("Maximum is", largest)
print("Mininum is", smallest)
