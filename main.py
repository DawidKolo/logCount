

def publicationCounting():

    publ = 0


    for n in range(1000000):

        file = open("data.txt", "r")
        data = file.read()

        a = " " + str(n) + " publications"

        occur = data.count(a)

        publ = publ + (occur * n)

    print(publ)

def docCounting():
    doc = 0

    for n in range(1000000):
        file = open("data.txt", "r")
        data = file.read()

        a = " " + str(n) + " documents"

        occur = data.count(a)

        doc = doc + (occur * n)

    print(doc)

def pageCount():
    page = 0

    for n in range(1000000):
        file = open("data.txt", "r")
        data = file.read()

        a = " " + str(n) + " pages"

        occur = data.count(a)

        page = page + (occur * n)

    print(page)

publicationCounting()
docCounting()
pageCount()
