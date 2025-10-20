from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Message and key
message = "Hello my friends"
key = b'mysecretaeskey12'  # 16 bytes key for AES-128

# Convert message to bytes and pad to multiple of 16
data = message.encode('utf-8')
padded_data = pad(data, AES.block_size)

# Generate a random IV (initialization vector)
iv = get_random_bytes(AES.block_size)

# Create AES cipher
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt
encrypted = cipher.encrypt(padded_data)
print("Encrypted (bytes):", encrypted)

# Decrypt
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(encrypted), AES.block_size)
print("Decrypted:", decrypted.decode('utf-8'))
