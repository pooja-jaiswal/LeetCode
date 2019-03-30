def reverse(x):
    if x == 0 or x >= 2147483647 or x<= -2147483648:
        return 0
    temp = str(x)
    while temp[len(temp)-1] == '0':
        temp = temp[:len(temp)-1]
    if x < 0:
        val = int('-'+temp[1:][::-1])
        if val<= -2147483648:
            return 0
        return val
    if int(temp[::-1]) >= 2147483647:
        return 0
    return int(temp[::-1])