# Given two words, beginWord and endWord, and a dictionary of words wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, such that:



# Only one letter can be changed at a time.



# Each transformed word must exist in the word list.






# Return 0 if no such sequence exists.


# All words have the same length and consist of lowercase letters only.


# beginWord is not considered a transformed word and may not be in wordList.
# Example:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5


def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = [(beginWord, 1)]  

    while queue:
        word, length = queue.pop(0)  

        if word == endWord:
            return length

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i+1:]
                if newWord in wordSet:
                    queue.append((newWord, length + 1))
                    wordSet.remove(newWord)

    return 0



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList)) 
