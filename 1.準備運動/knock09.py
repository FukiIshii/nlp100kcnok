# 09. Typoglycemia
# スペース区切りの単語列について、各単語の先頭と末尾の文字は残し、それ以外の文字をランダムに並べ替えよ。
# 長さ4以下の単語は並べ替えない。

import random

# %% 入力
text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# %% 処理（関数の定義）
def shuffle_word(word):
    """長さ5以上の単語について、先頭と末尾以外の文字をランダムに並べ替える"""
    if len(word) <= 4:
        return word
    middle = random.sample(word[1:-1], len(word) - 2)
    return word[0] + "".join(middle) + word[-1]


def typoglycemia(text):
    """スペース区切りの各単語にshuffle_wordを適用する"""
    return " ".join(shuffle_word(word) for word in text.split(" "))

# %% 実行と結果の表示（毎回同じ結果になるように乱数のシードを固定する）
random.seed(42)
result = typoglycemia(text)

print("元の文:", text)
print("並べ替え後:", result)
