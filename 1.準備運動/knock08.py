# 08. 暗号文

# 関数の定義
def cipher(text):
    result = ""
    for char in text:
        if "a" <= char <= "z":
            result += chr(219 - ord(char))
        else:
            result += char
    return result

# 実行と結果の表示（同じ関数をもう一度かけると元に戻る）
message = "Hello, NLP 2025! This is a secret message."
encrypted = cipher(message)
decrypted = cipher(encrypted)

print("元のメッセージ:", message)
print("暗号化:", encrypted)
print("復号化:", decrypted)
