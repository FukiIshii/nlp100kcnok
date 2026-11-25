# 02. 文字列の逆順
# "stressed" の文字を末尾から先頭に向かって並べた文字列を得よ。

# %% 入力
text = "stressed"

# %% 処理（ステップ -1 のスライスで末尾から順に取り出す）
result = text[::-1]

# %% 実行結果の表示
print("元の文字列:", text)
print("逆順の文字列:", result)
