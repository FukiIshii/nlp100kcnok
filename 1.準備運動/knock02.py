# 02. 文字列の逆順

# 入力
text = "stressed"

# 処理（1文字ずつ、resultの前に付け足していく）
result = ""

for char in text:
    result = char + result

# 結果の表示
print("元の文字列:", text)
print("逆順の文字列:", result)
