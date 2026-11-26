def make_ngram(sequence, n):
    result = []
    
    count = len(sequence) - n + 1
    
    for i in range(count):
        part = sequence[i:i + n]
        result.append(part)
        
    return result


word1 = "paraparaparadise"
word2 = "paragraph"

# 文字bi-gramのリストを作り、set()で集合（重複なし）に変換する
X = set(make_ngram(word1, 2))
Y = set(make_ngram(word2, 2))

print("X:", X)
print("Y:", Y)

# 和集合
wa = X | Y
print("和集合:", wa)

# 積集合
seki = X & Y
print("積集合:", seki)

# 差集合
sa = X - Y
print("差集合:", sa)

print("Xに'se'が含まれるか:", "se" in X)
print("Yに'se'が含まれるか:", "se" in Y)