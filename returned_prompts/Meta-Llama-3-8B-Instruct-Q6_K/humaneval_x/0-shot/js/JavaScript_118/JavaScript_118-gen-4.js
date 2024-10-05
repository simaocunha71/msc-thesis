Here is the JavaScript function that solves the problem:

```javascript
const getClosestVowel = (word) => {
    let vowels = 'aeiouAEIOU';
    let result = '';
    for (let i = word.length - 1; i > 0; i--) {
        if (vowels.includes(word[i])) {
            if (result === '' || vowels.includes(word[i - 1]) && vowels.includes(word[i + 1])) {
                result = word[i];
                break;
            }
        }
    }
    return result;
}
```

In this function, we iterate over the word from right to left. If we find a vowel, we check if the previous character is a consonant and the next character is a consonant. If this condition is met, we update the result and break the loop. If we didn't find any vowel that meets the condition, we return an empty string. The time complexity of this function is O(n), where n is the length of the word. The space complexity is O(1), as we are using a constant amount of space to store the vowels and the result.  */ 