# 00. パタトクカシーー

# 入力
str1 = "パトカー"
str2 = "タクシー"

# 処理
result = ""

for i in range(len(str1)):
    result += str1[i] + str2[i]

# 結果の表示
print("交互に連結した文字列:", result)
