def encrypt(text, key):
    result = ""
    key_length = len(key)
    key_as_int = [ord(i.upper()) - 65 for i in key]
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_as_int[i % key_length]
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    key_length = len(key)
    key_as_int = [ord(i.upper()) - 65 for i in key]
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_as_int[i % key_length]
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

message = input("Enter message: ")
key = input("Enter key: ")

encrypted = encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
