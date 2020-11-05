def countSubstrings(s):
    rez = 0
    n = len(s)
    for i in range(1, n+1)[::-1]:
        for i1 in range(len(s) + 1 - i):
            if s[i1:i1 + i] == s[i1:i1 + i][::-1]:
                rez += 1
    return rez

print(countSubstrings("abc"))
#print(countSubstrings("aaa"))