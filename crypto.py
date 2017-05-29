#! python3
# crypto.py
import re
import string

def cryptoDef():
    f = open('./random.txt', 'r');
    text = f.read();
    mo = re.split('(\W+)', text)
    invalidChars = [',', '.', ':', '?'];
    for index, char in enumerate(mo):
        if re.match('[a-zA-Z]', char):
            mo[index] = cryptWord(char);

    mo = "".join(mo);
    cryptoFile = open('randomcrypto.txt', 'w');
    cryptoFile.write(mo);
    f.close();
    cryptoFile.close();

def cryptWord(word):
    secretKey = 2;
    newWord = '';
    for char in word:
        newWord += chr(ord(char) + secretKey);

    return newWord;

cryptoDef();
