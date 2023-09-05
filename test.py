flag_register = 0x14
print(bin(flag_register))
mask = 8
print(bin(mask))
flag = flag_register & mask
print(bool(flag))
# flag_register &= mask
# print(bin(flag_register))

if flag_register & mask:
    # My bit is set.
    flag_register = flag_register & ~mask
else:
    # My bit is reset.
    flag_register = flag_register & mask

print(flag_register)
