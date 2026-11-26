# 03. 円周率

# 入力
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 処理（カンマとピリオドを取り除いてから文字数を数える）
words = text.split()
result = []

for word in words:
    result.append(len(word.strip(",.")))

# 結果の表示
print("各単語の文字数:", result)
