# 06. 集合

# 入力
text1 = "paraparaparadise"
text2 = "paragraph"

# 関数の定義（05と同じ）
def ngram(sequence, n):
    result = []
    for i in range(len(sequence) - n + 1):
        result.append(sequence[i:i + n])
    return result

# 処理
X = set(ngram(text1, 2))
Y = set(ngram(text2, 2))

# 結果の表示（setは表示順が毎回変わるので、sortedで並べてから表示する）
print("X:", sorted(X))
print("Y:", sorted(Y))
print("和集合 X∪Y:", sorted(X | Y))
print("積集合 X∩Y:", sorted(X & Y))
print("差集合 X−Y:", sorted(X - Y))
print("'se' がXに含まれるか:", "se" in X)
print("'se' がYに含まれるか:", "se" in Y)
