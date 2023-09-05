blocks = int(input("Enter the number of blocks: "))
height = 0
required_blocks = 1
#
# Write your code here.
#

while True:
    if required_blocks > blocks:
        break
    else:
        height += 1
        blocks -= required_blocks
        required_blocks += 1

print("The height of the pyramid:", height)

