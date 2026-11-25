# 04. 元素記号
# 文を単語に分解し、1,5,6,7,8,9,15,16,19番目の単語は先頭1文字、それ以外は先頭2文字を取り出し、
# 取り出した文字列から単語の位置（1始まり）への辞書を作れ。

# %% 入力
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_char_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}

# %% 処理（単語の位置によって、取り出す文字数を1文字か2文字に切り替える）
symbol_to_position = {}
for position, word in enumerate(text.split(), start=1):
    n_chars = 1 if position in one_char_positions else 2
    symbol_to_position[word[:n_chars]] = position

# %% 実行結果の表示
print("要素数:", len(symbol_to_position))
print("元素記号 → 単語の位置:", symbol_to_position)
