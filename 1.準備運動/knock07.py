# 07. テンプレートによる文生成

# 関数の定義
def make_sentence(x, y, z):
    return f"{x}時の{y}は{z}"

# 実行と結果の表示
result = make_sentence(12, "気温", 22.4)
print("生成した文:", result)
