import cv2
import os
import string

img = cv2.imread("Bird.jpg")

msg = input("Enter Privet Message:")
Password = input("Enter ypur Password:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

l = 0
m = 0
n = 0

for i in range(len(msg)):
    img[m, l, n] = d[msg[i]]
    m = m + 1
    l = l + 1
    n = (n + 1) % 3

cv2.imwrite("EncryptedImage.jpg", img)
os.system("start EncryptedImage.jpg")
