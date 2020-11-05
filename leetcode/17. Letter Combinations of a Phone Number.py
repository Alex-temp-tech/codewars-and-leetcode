import itertools
def letterCombinations(digits):
    n_l = len(str(digits))
    rez = []
    dic_n = {2: ["a","b","c"], 3: ["d","e","f"], 4: ["g","h","i"],5: ["j", "k", "l"],6: ["m","n","o"], 7: ["p","q","r","s"],8: ["t","u","v"],9: ["w","x","y","z"]}
    t1 = dic_n[2]
    t2 = dic_n[3] + "a"
    #t1 = list(itertools.combinations(t1,2))
    t2 = list(itertools.combinations(t2, 2))
    return t2


print(letterCombinations(23))
