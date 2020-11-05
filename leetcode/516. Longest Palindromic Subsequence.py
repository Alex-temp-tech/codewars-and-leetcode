import collections
def longestPalindromeSubseq(s):
    t1 = collections.Counter(s).most_common()
    print(t1)
    #return t1[0][1]
print(longestPalindromeSubseq("cbbd"))
print(longestPalindromeSubseq("bbbab"))#4
print(longestPalindromeSubseq("aabaa"))#5
print(longestPalindromeSubseq("abab"))#3
