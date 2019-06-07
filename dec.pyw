import base64
import datetime
import os
import pandas as pd


def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()

    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)

    return "".join(dec)


defkey = 'thisIsTheKey'
run = 1

while run:

    act = int(input("1 to encode , 2 to decode, 3 to decode .txt file, 9 to quit "))

    if act == 1:

        wordtoencode = input("enter word to encode ")

        key = input("enter key or 0 to use default key ")

        if key == '0':

            key = defkey

        else:

            pass

        enc = encode(key, wordtoencode)

        print (enc)
#
    if act == 2:

        encodedstr = input("enter decoded word ")

        key = input("enter key or 0 to use default key ")

        if key == '0':
            key = defkey

        dec = decode(key, encodedstr)

        sav = int(input("save to log.txt? 1/0"))

        if sav == 1:
            today = datetime.datetime.now()

            with open("log.txt", "a") as text_file:
                text_file.write(" Date : " + str(datetime.datetime.now()) + " entry: " + dec + "\n")

        print (dec)

    if act == 3:

        # select file

        print(os.listdir())

        tx = input("select text file name: (for example log)")

        # load text file to decrypt

        data = pd.read_csv(tx + ".txt", sep=" ", header=None, usecols=[3, 4, 6])

        # the key to decryption

        key = input("enter key or 0 to use default key ")

        if key == '0':
            key = defkey

        data["decrypted"] = data[6].apply(lambda x: decode(key, x))

        data.loc[:, data.columns != 6].to_csv("decrypted.txt", index=False, header=None)

    if act == 9:
        run = 0

