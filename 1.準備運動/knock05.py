# 05. n-gram
# シーケンス（文字列やリスト）からn-gramを作る関数を作り、
# "I am an NLPer" から文字tri-gramと単語bi-gramを得よ。

# %% 入力
text = "I am an NLPer"

# %% 処理（関数の定義）
def ngram(sequence, n):
    """文字列やリストから、長さnの連続した部分列をすべて取り出す"""
    return [sequence[i:i + n] for i in range(len(sequence) - n + 1)]

# %% 実行と結果の表示
char_trigrams = ngram(text, 3)          # 文字列を渡すと文字n-gram
word_bigrams = ngram(text.split(), 2)   # 単語のリストを渡すと単語n-gram

print("文字tri-gram:", char_trigrams)
print("単語bi-gram:", word_bigrams)
