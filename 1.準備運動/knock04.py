# 04. 元素記号

# 入力
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_char = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# 処理（iは0始まりなので、単語の位置は i + 1）
words = text.split()
result = {}

for i in range(len(words)):
    if i + 1 in one_char:
        result[words[i][:1]] = i + 1
    else:
        result[words[i][:2]] = i + 1

# 結果の表示
print("元素記号 → 単語の位置:", result)
