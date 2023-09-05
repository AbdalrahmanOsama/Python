var = 9
print(format(var, '08b'))
var_right = var >> 1
print(format(var_right, '08b'))
varright = var // 2
var_left = var << 2
print(format(var_left, '08b'))
varleft = var * 4
print(var, var_left, varleft, var_right, varright)
