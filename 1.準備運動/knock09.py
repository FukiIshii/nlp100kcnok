# 09. Typoglycemia

import random

# 関数の定義
def shuffle_word(word):
    if len(word) <= 4:
        return word

    middle = list(word[1:-1])
    random.shuffle(middle)

    return word[0] + "".join(middle) + word[-1]

# 実行と結果の表示（毎回同じ結果になるようにseedを固定する）
random.seed(42)

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = text.split()
result = []

for word in words:
    result.append(shuffle_word(word))

print("元の文:", text)
print("並べ替え後:", " ".join(result))
