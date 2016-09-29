fin = open("C:\Users\scott\Downloads\words.txt")
for line fin:
    word = line.strip()
    if len(word) > 20:
        print word
