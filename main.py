import re


def pubCount():
# open log file
    s = open("data.txt", "r")
    data = s.read()

# define pattern to search
    pattern = r"(\d+) publications"

# find all occurences of pattern
    matches = re.findall(pattern,data)
    newList = [eval(i) for i in matches]

    print("The number of the publications: " + str(sum(newList)))

def docCount():
    s = open("data.txt", "r")
    data = s.read()

    pattern = r"(\d+) documents"

    matches = re.findall(pattern, data)
    newList = [eval(i) for i in matches]

    print("The number of the documents: " + str(sum(newList)))

def pageCount():
    s = open("data.txt", "r")
    data = s.read()

    pattern = r"(\d+) pages"

    matches = re.findall(pattern, data)
    newList = [eval(i) for i in matches]

    print("The number of pages: "+str(sum(newList)))

pubCount()
docCount()
pageCount()




