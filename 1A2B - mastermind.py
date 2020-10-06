# 數三甲 40640102S 林以寧
# 遊戲演算法 ex5-1

# Mastermind

# 以下程式開始

# 生成所有答案的 Set
S = set()
gene_A = []
n = 6 # int(input("n = ")) # Mastermind 有六種顏色
m = 4 # int(input("m = "))
for i in range(m) :
    gene_A = gene_A + [1]

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
        if gene_A[i] < n :
            break
        i = i-1
    if i != -1 :
        gene_A[i] = gene_A[i]+1
        for j in range(i+1,m) :
            gene_A[j] = gene_A[j-1]
    else :
        break
print("原始 S(所有可能解) 有 {} 個".format(len(S)))

# 找出相符答案的函式
def find(X, Y, n=4, A=0, B=0):
    for i in set(X):
        if Y.count(i) > 0:
            B += min(X.count(i),Y.count(i))
    for j in range(len(X)):
        if X[j] == Y[j]:
            A += 1
            B -= 1
    return (A,B)

# 開始猜~
Final_Guess = "1122" # 第一個直接指定
for guess_times in range(5):
    print(Final_Guess)
    A = int(input("A = "))
    B = int(input("B = "))
    
    # 刪除不合的答案
    S_copy = S.copy()
    for obj in S_copy:
        if find(Final_Guess,obj) != (A,B):
            S.remove(obj)
    if len(S) <= 1:
        break
    print("S 剩 {} 個".format(len(S)))

    # Knuth 評分
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
            final_guess = MIN.get(key)
            Final_Guess = key # 找到下一次猜測

# 第一個就用 Knuth 的找法
"""
for guess_times in range(5):
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
            final_guess = MIN.get(key)
            Final_Guess = key

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
    print("S 剩 {} 個".format(len(S)))
"""
print(S)
    

