from os import path
from sys import exit
from string import ascii_lowercase, ascii_uppercase

if not path.isfile("lyrics.txt"):
    exit("Please save the lyrics in a text file with the name: lyrics.txt")
lyrics = open("lyrics.txt")
lyric_dict = {}

for i in lyrics:
    if i.startswith("["):
        continue
    else:
        temparray = i.split(" ")
        for j in temparray:
            for l in j:
                if l in ascii_uppercase:
                    t = ascii_uppercase.split(l)
                    t2 = len(t[0])
                    j = j.replace(ascii_uppercase[t2], ascii_lowercase[t2])
            if "\n" in j:
                j = j[:-1]
                print("adjusted paragraph")
            if "(" in j:
                j = j[1:]
                print("adjusted comment")
            if ")" in j:
                j = j[:-1]
                print("adjusted comment")
                                #needs some work
            if "," in j:
                j = j[:-1]
                print("adjusted comma")
            if "!" in j:
                j = j[:-1]
                print("adjusted exclamation mark")
            if "?" in j:
                j = j[:-1]
                print("adjusted question mark")
            if j in lyric_dict:
                lyric_dict[j] = lyric_dict[j] + 1
            else:
                lyric_dict[j] = 1

lyrics.close()
if "" in lyric_dict:
    lyric_dict.pop("")
if "-" in lyric_dict:
    lyric_dict.pop("-")
lyric_analyse = open("lyric_analyse.txt", "w")
for i in reversed(sorted(lyric_dict, key=lyric_dict.get)):
    lyric_analyse.write(i + ": " + str(lyric_dict[i]) + "\n")
lyric_analyse.close()

sum = 0
for k in lyric_dict:
    sum = sum + lyric_dict[k]

print("analyzed ", sum, " words")
x = input("created lyric_analyse.txt\n")