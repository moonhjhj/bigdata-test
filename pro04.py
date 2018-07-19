from collections import Counter

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""


s = s.upper().replace(",", "").replace(".", "").replace("\n", "").split()

wordDicts = set([])

for word in s:
    count_word = s.count(word)
    wordDicts.add(word + " : %d" %count_word)

wordList = []
for wordDict in wordDicts:
    wordList.append(wordDict)
    wordList.sort()

for final in wordList:
    print(final)

