from StegoEncryption import Password
from StegoEncryption import msg
from StegoEncryption import img
from StegoEncryption import c

Message = ""
m = 0
l = 0
n = 0
Pas = input("Enter Password for Decryption: ")
if Password == Pas:
    for i in range(len(msg)):
        Message = Message + c[img[m, l, n]]
        m = m + 1
        l = l + 1
        n = (n + 1) % 3
    print("Decrypted Message:", Message)
else:
    print("YOU ARE NOT auth")

