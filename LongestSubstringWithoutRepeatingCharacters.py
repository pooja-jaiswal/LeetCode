def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    longest = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen: break
            seen.add(s[j])
        longest = max(len(seen), longest)
    return longest