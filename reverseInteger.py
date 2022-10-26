def reverseInteger(num):
    convert = list(str(num))
    sign = False
    if(num < 0):
        sign = True
        convert.pop(0)
    convert.reverse()
    transform = int(''.join(convert))
    if transform >= 2**31-1 or transform <= -2**31:
        transform = 0
    return '{tag}{num}'.format(tag = '-' if sign and transform != 0 else '', num = transform)

print(reverseInteger(int(input())))