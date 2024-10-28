    var maxWord string
    var maxCount int

    for _, word := range words {
        count := 0
        for _, w := range word {
            if !contains(word, w) {
                count++
            }
        }
        if count > maxCount {
            maxCount = count
            maxWord = word
        } else if count == maxCount && word < maxWord {
            maxWord = word
        }
    }
    return maxWord
}

func contains(word string, c byte) bool {
    for _, w := range word {
        if w == c {
            return true
        }
    }
    return false
}

To solve this problem, we can follow a brute force approach, but it's slow.
We can sort the list of words in descending order of their unique character count.
Once sorted, we can return the first element of the slice, which will have maximum unique characters.
This approach is O(nlogn).

But, we can optimize it further to O(n).
For each word, we can count the number of unique characters.
If the count is greater than the maximum count till now, update maxCount and maxWord.
If the count is equal to maxCount, and the word comes first in lexicographical order, update maxWord.
Finally, return maxWord.

The contains function is used to check if a character exists in a word.
It's used in the contains function to check if a character exists in a word.

The time complexity of the contains function is O(len(word)).
The time complexity of the FindMax function is O(n).

Here is a Python equivalent of the solution.

def findMax(words):
    maxWord = ""
    maxCount = 0
    for word in words:
        count = 0
        for c in word:
            if c not in word:
                count += 1
        if count > maxCount:
            maxCount = count
            maxWord = word
        elif count == maxCount and word < maxWord:
            maxWord = word
    return maxWord

def contains(word, c):
    for w in word:
        if w == c:
           