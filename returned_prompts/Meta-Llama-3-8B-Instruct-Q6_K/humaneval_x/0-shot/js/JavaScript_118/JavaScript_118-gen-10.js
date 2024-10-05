Here is a JavaScript solution for the problem:

```javascript
const getClosestVowel = (word) => {
    let result = '';
    for (let i = word.length - 1; i > 0; i--) {
        if ('aeiouAEIOU'.includes(word[i])) {
            if (result === '') {
                result = word[i];
            } else if ('aeiouAEIOU'.includes(word[i - 1])) {
                return result;
            } else {
                return word[i];
            }
        }
    }
    return result;
}
```

This function iterates over the word from right to left. It checks each character if it is a vowel. If it is a vowel and the result variable is empty, it sets the result to the current vowel. If the result is not empty and the previous character is also a vowel, it returns the result. If the previous character is not a vowel, it returns the current vowel. If it doesn't find any vowel that stands between two consonants, it returns the last vowel it found. If it doesn't find any vowel at all, it returns an empty string. 