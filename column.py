#!/usr/bin/python3

def splitNewlines(line, colomnWidth):
    index = colomnWidth + 1
    index = line.rfind(' ', 0, index)
    return line[:index] + "\n" + line[index+1:]

text="per ole"
res = splitNewlines(text, 3)
#print(res)
assert res == "per\nole"

