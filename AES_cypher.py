e{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww28600\viewh15220\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 AES Cypher
\f1\fs24 \

\f0\fs29\fsmilli14667 Python Script
\f1\fs24 \
\
\
\pard\pardeftab720\sa320\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 from Crypto.Cipher import AES
\f1\fs24 \

\f0\fs29\fsmilli14667 from Crypto.Random import get_random_bytes
\f1\fs24 \

\f0\fs29\fsmilli14667 from Crypto.Util.Padding import pad, unpad
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa320\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 text = input("Enter message: ")
\f1\fs24 \

\f0\fs29\fsmilli14667 key = input("Enter 16-character key: ").encode('utf-8')
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa320\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 data = pad(text.encode('utf-8'), AES.block_size)
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa320\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 iv = get_random_bytes(AES.block_size)
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa320\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 cipher = AES.new(key, AES.MODE_CBC, iv)
\f1\fs24 \

\f0\fs29\fsmilli14667 encrypted = cipher.encrypt(data)
\f1\fs24 \

\f0\fs29\fsmilli14667 print("Encrypted message:", encrypted)
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa320\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 cipher2 = AES.new(key, AES.MODE_CBC, iv)
\f1\fs24 \

\f0\fs29\fsmilli14667 decrypted = unpad(cipher2.decrypt(encrypted), AES.block_size)
\f1\fs24 \

\f0\fs29\fsmilli14667 print("Decrypted message:", decrypted.decode('utf-8'))
\f1\fs24 \

