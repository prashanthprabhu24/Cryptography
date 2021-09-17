import pprint
def getWordPattern(word):
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []
    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])

    return '.'.join(wordPattern)

def main():
    allPatterns = {}
    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()
    for word in wordList:
        pattern = getWordPattern(word)
        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)
    fo = open('wordpattern.py','w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()

if __name__ == '__main__':
    main()







