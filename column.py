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

def addSpacesInLine(line, colomnWidth):
    index = 0
    if(line.find(' ', index) < 0):
       return line
       
    while(len(line) < colomnWidth):
        index = line.find(' ', index)
        if(index >= 0):
            line = line[:index] + " " + line[index:]
            index += 2
        else:
            index = 0        
    return line

def addSpaces(lines, colomnWidth):
    splitLines = lines.splitlines()
    retLine = ""
    for line in splitLines:
        retLine += addSpacesInLine(line, colomnWidth) + "\n"
    return retLine

def makeColumns(line, colomnWidth):
    return addSpaces(splitNewlines(line, colomnWidth), colomnWidth)


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

text="xx yy\n"
res = addSpaces(text, 5)
assert res == "xx yy\n"

text="xx yy\n"
res = addSpaces(text, 6)
assert res == "xx  yy\n"

text="xx yy\nzz\n"
res = addSpaces(text, 5)
#print(res)
assert res == "xx yy\nzz\n"

text="xx yy zz"
res = makeColumns(text, 6)
#print(res)
assert res == "xx  yy\nzz\n"

text="xx yy zz"
res = makeColumns(text, 10)
#print(res)
assert res == "xx  yy  zz\n"

#text="reporters on Saturday was"
#res = addSpacesInLine(text, 30)
#print("0123456789 123456789 123456789")
#print(res)

text="Conley also said that Chief of Staff Mark Meadows' update to reporters on Saturday was misconstrued, adding that the chief and I work side by side. The president's vitals over the last 24 hours were very concerning and the next 48 hours will be critical in terms of his care. We're still not on a clear path to a full recovery, Meadows said. The doctor confirmed that Meadows was referencing the president's high fever and oxygen drop 24 hours earlier. Trump shared a video message from hospital on Saturday evening, warning the next few days will be the real test in his fight against the killer bug."

res = makeColumns(text, 30)
print(res)
