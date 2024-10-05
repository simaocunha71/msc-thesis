Here is a JavaScript function to solve this problem:

```javascript
const getClosestVowel = (word) => {
    let result = "";
    for (let i = word.length - 1; i > 0; i--) {
        if (["a", "e", "i", "o", "u"].includes(word[i].toLowerCase())) {
            if (word[i - 1].toLowerCase() !== "a" && word[i - 1].toLowerCase() !== "e" && word[i - 1].toLowerCase() !== "i" && word[i - 1].toLowerCase() !== "o" && word[i - 1].toLowerCase() !== "u") {
                result = word[i].toLowerCase();
                break;
            }
        }
    }
    return result;
}
```

In this function, we are iterating over the word from right to left. If we find a vowel, we check if the previous character is a vowel or not. If it is not a vowel, we consider this vowel as the closest one and break the loop. If we don't find any vowel that meets the condition, we return an empty string. The function is case-insensitive because we convert the characters to lowercase before comparing.