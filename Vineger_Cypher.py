def encrypt(text, key):
result = ''
key = key.lower()
key_index = 0
for c in text:
if c.isalpha():
shift = ord(key[key_index % len(key)]) - ord('a')
base = ord('A') if c.isupper() else ord('a')
result += chr((ord(c) - base + shift) % 26 + base)
key_index += 1
else:
result += c
return result

def decrypt(text, key):
result = ''
key = key.lower()
key_index = 0

for c in text:
if c.isalpha():
shift = ord(key[key_index % len(key)]) - ord('a')
base = ord('A') if c.isupper() else ord('a')
result += chr((ord(c) - base - shift) % 26 + base)
key_index += 1
else:
result += c
return result

text = input("Enter text: ")
key = input("Enter key: ")

encrypted = encrypt(text, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
