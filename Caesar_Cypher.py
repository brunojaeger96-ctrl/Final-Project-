text = input("Enter text: ")
key = int(input("Enter key: "))
result = ''

for c in text:
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        result += chr((ord(c) - base + key) % 26 + base)
    else:
        result += c

print("Encrypted text:", result)
