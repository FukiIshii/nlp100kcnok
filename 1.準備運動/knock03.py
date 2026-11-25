# 03. 円周率
# "Now I need a drink, ... quantum mechanics." を単語に分解し、
# 各単語の（アルファベットの）文字数を出現順に並べたリストを作れ。

# %% 入力
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# %% 処理（単語に分解し、アルファベットだけを数える）
words = text.split()
lengths = [sum(c.isalpha() for c in word) for word in words]

# %% 実行結果の表示
print("単語のリスト:", words)
print("各単語の文字数:", lengths)
