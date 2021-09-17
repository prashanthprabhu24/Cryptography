UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTER_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()
def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches)/len(possibleWords)
def removeNonLetters(message):
    letterOnly = []
    for symbol in message:
        if symbol in LETTER_AND_SPACE:
            letterOnly.append(symbol)
    return ''.join(letterOnly)

def isEnglish(messaage, wordPercentage=20,letterPercentage=85):
    wordMatch = getEnglishCount(messaage) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(messaage))
    messaageLetterspercentage = float(numLetters)/len(messaage) * 100
    lettersMatch = messaageLetterspercentage >= letterPercentage
    return  wordMatch and lettersMatch
