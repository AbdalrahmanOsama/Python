c0 = int(input("Enter a value: "))
steps = 0

while c0 != 1:
    if (c0 % 2) == 0:   #even
        c0 /= 2
        steps += 1
        print(int(c0))

    else:               #odd
        c0 = c0 * 3 + 1
        steps += 1
        print(int(c0))

print("Steps= " + str(steps))
