def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if str(x) == str(x)[::-1]:
        val = True
    else:
        val = False
    return val