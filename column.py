#!/usr/bin/python3
#import time

def splitNewlines(line, colomnWidth):
    index = colomnWidth + 1
    while index < len(line):
        index = line.rfind(' ', 0, index)
        line = line[:index] + "\n" + line[index+1:]
        index += colomnWidth + 2
        #time.sleep(2)
    return line

def addSpaces(lines, colomnWidth):
    return lines
    

text="per ole"
res = splitNewlines(text, 3)
#print(res)
assert res == "per\nole"

text="xx yy zz"
res = splitNewlines(text, 2)
#print(res)
assert res == "xx\nyy\nzz"

text="xx yy zz"
res = splitNewlines(text, 3)
#print(res)
assert res == "xx\nyy\nzz"

text="xx yy zz"
res = splitNewlines(text, 5)
#print(res)
assert res == "xx yy\nzz"

text="xx yy zz"
res = splitNewlines(text, 6)
#print(res)
assert res == "xx yy\nzz"

text="xx yy\nzz"
res = addSpaces(text, 5)
assert res == "xx yy\nzz"
