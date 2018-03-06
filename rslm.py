from random import randint

def random_words(nmin, nmax):    
    w = []
    wordlist = []

    with open("words.txt", "r") as words:
        for i in words:
           w.append(i)

    for i in range(nmin, nmax):
        x = randint(0, len(w))
        word = w[x].strip()
        wordlist.append(word)

    return wordlist
