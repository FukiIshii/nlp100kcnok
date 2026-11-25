# 06. 集合
# "paraparaparadise" と "paragraph" の文字bi-gramの集合をX, Yとし、和集合・積集合・差集合を求めよ。
# さらに 'se' がXおよびYに含まれるか調べよ。

# %% 入力
text1 = "paraparaparadise"
text2 = "paragraph"

# %% 処理（関数の定義：05と同じもの）
def ngram(sequence, n):
    """文字列やリストから、長さnの連続した部分列をすべて取り出す"""
    return [sequence[i:i + n] for i in range(len(sequence) - n + 1)]

# %% 処理（bi-gramの集合を作り、集合演算を行う）
X = set(ngram(text1, 2))
Y = set(ngram(text2, 2))

union = X | Y
intersection = X & Y
difference = X - Y

# %% 実行結果の表示（集合は順序を持たないので、sortedで並べて表示する）
print("X:", sorted(X))
print("Y:", sorted(Y))
print("和集合 X∪Y:", sorted(union))
print("積集合 X∩Y:", sorted(intersection))
print("差集合 X−Y:", sorted(difference))
print("'se' がXに含まれるか:", "se" in X)
print("'se' がYに含まれるか:", "se" in Y)
