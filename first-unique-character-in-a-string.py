import collections
def firstUniqChar(s):
    s = "testcodetest"
    count = collections.Counter(s)
    for i, each in enumerate(s):
        if count[each] == 1:
            return i     
    return -1