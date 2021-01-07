import random
from datetime import datetime
def displayText():
    with open("tests.txt", "r") as f:
        txt = random.choice(f.read().split('\n'))
        print(f'Type this as fast as possible:\n{txt}')
    return txt.split(" ")

def checkMistakes(inp: list, correct: list):
    mistakes = 0
    for i, c in zip(inp, correct):
        if i != c:
            mistakes += 1
    return mistakes

def fillOutEmptyElements(inp: list, correct: list):
    a = inp
    temp = []
    for i in range(len(correct)):
        try:
            temp.append(inp[i])
        except:
            a.append(0)
    return a

def calculateWPM(words: int, time: float):
    wpm = int((words / time) * 60)
    return wpm

def main():
    correct = displayText()
    bef = datetime.now().timestamp()
    inp = input("--->  ").split(" ")
    aft = datetime.now().timestamp()
    time = aft - bef
    amountOfCorrectWords = len(correct) - checkMistakes(fillOutEmptyElements(inp, correct), correct)
    print(f'Your WPM (words per minute) is {calculateWPM(amountOfCorrectWords, time)}')

if __name__ == '__main__':
    main()
