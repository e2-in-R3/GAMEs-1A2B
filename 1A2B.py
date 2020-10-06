# 數三甲 40640102S 林以寧
# 遊戲演算法 ex5-1

# 1A2B

# 以下程式開始
from random import choice

S = set()

# 生成所有答案的 Set
gene_A = []

n = 9 # int(input("n = "))
m = 4 # int(input("m = "))
for i in range(m) :
    gene_A = gene_A + [i]

while True :
    B = list(gene_A)
    while True :
        # 用字典序排列{
        # 換成字串存入 Set
        L = ""
        for l in range(len(B)):
            L += str(B[l])
        S = S | {L} 
        
        for i in range(m-1,0,-1) :
            if B[i] > B[i-1] :
                p = i-1
                break
            if i == 1 :
                p = -1

        if p != -1 :
            for j in range(m-1,p,-1) :
                if B[j] > B[p] :
                    B[p], B[j] = B[j], B[p]
                    for k in range(p+1,m) :
                        for l in range(k,m) :
                            if B[k] > B[l] :
                                B[k], B[l] = B[l], B[k]
                    break
        else :
            break
        # 用字典序排列}
    i = m-1
    while i != -1 :
        if gene_A[i] < n-m+i+1 :
            break
        i = i-1
    if i != -1 :
        gene_A[i] = gene_A[i]+1
        for j in range(i+1,m) :
            gene_A[j] = gene_A[j-1]+1
    else :
        break

# 找出相符答案的函式
def find(X, Y, n=4, A=0, B=0):
    for i in range(n):
        if X[i] in Y :
            B += 1
            if X[i] == Y[i]:
                A += 1
                B -= 1
    return (A,B)

#"""
Final_Guess = 0
for guess_times in range(7):
    if Final_Guess == 0:
        Final_Guess = choice(list(S))
    print(Final_Guess)
    A = int(input("A = "))
    B = int(input("B = "))
    # 刪除不合的答案
    S_copy = S.copy()
    for obj in S_copy:
        if find(Final_Guess,obj) != (A,B):
            S.remove(obj)
    if len(S) == 1:
        break
    print(len(S))

    MIN = dict()
    for i in S: # 猜 i
        MAX = 0
        # 與 j 關係 (0,0)~(2,2)
        for a in range(3):
            for b in range(4-a):
                S_copy = S.copy()
                for obj in S:
                    if find(i,obj) != (a,b):
                        S_copy.remove(obj)
                if MAX < len(S_copy):
                    MAX = len(S_copy)
        # 與 j 關係 (3,0)~(3,1)
        a = 3
        for b in range(2):
            S_copy = S.copy()
            for obj in S:
                if find(i,obj) != (a,b):
                    S_copy.remove(obj)
            if MAX < len(S_copy):
                MAX = len(S_copy)
        # 與 j 關係 (4,0)
        S_copy = S.copy()
        for obj in S:
            if find(i,obj) != (a,b):
                S_copy.remove(obj)
        if MAX < len(S_copy):
            MAX = len(S_copy)
        MIN[i] = int(MAX)
    final_guess = 10000
    for key in MIN:
        if MIN.get(key) < final_guess:
            Final_Guess = key
#""" # 2 優化

"""
g = 0
for guess in range(7):
    # g = choice(list(S))
    if g == 0:
        g = choice(list(S))
    print(g)
    A = int(input("A = "))
    B = int(input("B = "))
    # 刪除不合的答案
    S_copy = S.copy()
    for obj in S_copy:
        if find(g,obj) != (A,B):
            S.remove(obj)
    if len(S) == 1:
        break
    
    S_i = 0
    S_j = set()
    for i in S: # 猜 i
        for j in S: # 答案為 j
            S_copy = S.copy()
            ij = find(i,j)
            for obj in S:
                if find(i,obj) == ij:
                    S_copy.remove(obj) # 只留下應該被刪掉的
            S_j = S_j | {len(S_copy)}
        if min(S_j) >= S_i:
            S_i = min(S_j)
            Si = i
    g = Si
""" # 1 優化
"""
for guess in range(7):
    g = choice(list(S))
    print(g)
    A = int(input("A = "))
    B = int(input("B = "))
    # 刪除不合的答案
    S_copy = S.copy()
    for obj in S_copy:
        if find(g,obj) != (A,B):
            S.remove(obj)
    if len(S) == 1:
        break
""" # 0 優化
print(S)
    

