import re


def Count():
    patternList = ['publications', 'documents', 'pages']
# open log file
    s = open("data.txt", "r")
    data = s.read()
    for i in patternList:

# define pattern to search
        pattern = r"(\d+) "+ i

# find all occurences of pattern
        matches = re.findall(pattern,data)
        newList = [eval(i) for i in matches]

        print("The number of the "+ i + " " + str(sum(newList)))


Count()




