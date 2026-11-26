# 05. n-gram

# 入力
text = "I am an NLPer"

# 関数の定義
def ngram(sequence, n):
    result = []
    for i in range(len(sequence) - n + 1):
        result.append(sequence[i:i + n])
    return result

# 実行と結果の表示（文字列を渡すと文字n-gram、単語のリストを渡すと単語n-gram）
char_trigram = ngram(text, 3)
word_bigram = ngram(text.split(), 2)

print("文字tri-gram:", char_trigram)
print("単語bi-gram:", word_bigram)
