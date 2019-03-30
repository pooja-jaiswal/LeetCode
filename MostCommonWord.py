def mostCommonWord(paragraph, banned):
    banset = set(banned)
    count = collections.Counter(
        word.strip("!?',;.") for word in paragraph.lower().split())

    ans, best = '', 0
    for word in count:
        if count[word] > best and word not in banset:
            ans, best = word, count[word]

    return ans

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))