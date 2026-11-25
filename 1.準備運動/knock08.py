# 08. 暗号文
# 英小文字なら (219 - 文字コード) の文字に置換、それ以外はそのままにする関数cipherを作り、
# 英語のメッセージを暗号化・復号化せよ。

# %% 入力
message = "Hello, NLP 2025! This is a secret message."

# %% 処理（関数の定義）
def cipher(text):
    """英小文字だけを (219 - 文字コード) の文字に置き換える"""
    return "".join(chr(219 - ord(c)) if "a" <= c <= "z" else c for c in text)

# %% 実行と結果の表示（復号化にも同じ関数を使う）
encrypted = cipher(message)
decrypted = cipher(encrypted)

print("元のメッセージ:", message)
print("暗号化:", encrypted)
print("復号化:", decrypted)
print("元に戻ったか:", decrypted == message)
