def cipher(text):
    result = ""
    
    for char in text:
        if "a" <= char <= "z":
            code = 219 - ord(char)
            result += chr(code)
        else:
            result += char
            
    return result

message = "Hello! こんにちは。"

encrypted = cipher(message)
print("暗号化:", encrypted)

decrypted = cipher(encrypted)
print("復号化:", decrypted)