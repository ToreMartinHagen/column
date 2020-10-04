#!/usr/bin/python3

def splitNewlines(line, colomnWidth):
    index = colomnWidth
    index = line.rfind(' ', index)
    return line[:index] + "\n" + line[index+1:]

text="per ole"
res = splitNewlines(text, 3)
#print(res)
assert res == "per\nole"
