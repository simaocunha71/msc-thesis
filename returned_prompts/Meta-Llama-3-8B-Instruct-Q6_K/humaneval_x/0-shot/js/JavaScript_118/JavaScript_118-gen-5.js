Here is a JavaScript solution for the problem:

```javascript
const getClosestVowel = (word) => {
    for (let i = word.length - 1; i >= 0; i--) {
        if (['a', 'e', 'i', 'o', 'u'].includes(word[i].toLowerCase())) {
            for (let j = i - 1; j >= 0; j--) {
                if (!['a', 'e', 'i', 'o', 'u'].includes(word[j].toLowerCase())) {
                    return word[i].toLowerCase();
                }
            }
        }
    }
    return '';
};
```

This function iterates over the word from right to left. If it finds a vowel, it then iterates over the characters to the left of the vowel to find the first consonant. It returns the vowel if it finds one. If it doesn't find any vowel or vowel is at the beginning of the word, it returns an empty string. The function is case-insensitive. It converts each character to lowercase before checking if it's a vowel.

The time complexity of this function is O(n), where n is the length of the word. This is because in the worst case, we are iterating over the entire word. The space complexity is O(1), as we are using a constant amount of space to store the vowels and the indices. 