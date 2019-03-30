# def reverseString(s):
#     n = len(s)
#     temp = []
#     for each in range(n-1, -1,-1):
#        s += temp[each]




def reverseString(s):
    n = len(s)
    start = 0
    end = n - 1
    while start < end: 
        s[start], s[end] = s[end], s[start] 
        start += 1
        end -= 1
    print(s)

print(reverseString(["h","e","l","l","o"]))