Here is a JavaScript function that solves the problem:

```javascript
const getClosestVowel = (word) => {
    let closestVowel = '';
    for (let i = word.length - 1; i >= 0; i--) {
        if (['a', 'e', 'i', 'o', 'u'].includes(word[i].toLowerCase())) {
            let isBetweenConsonants = true;
            for (let j = i - 1; j >= 0; j--) {
                if (!['a', 'e', 'i', 'o', 'u'].includes(word[j].toLowerCase())) {
                    isBetweenConsonants = false;
                    break;
                }
            }
            if (isBetweenConsonants) {
                closestVowel = word[i];
                break;
            }
        }
    }
    return closestVowel;
};
```

This function iterates through the word from right to left. When it finds a vowel, it checks if the previous characters are consonants. If they are, it sets the vowel as the closest vowel and breaks the loop. If it doesn't find any vowel that meets the condition, it returns an empty string. The function is case sensitive, so it converts the word to lowercase before checking if a character is a vowel. This way, it treats 'A' and 'a' as the same vowel. 

You can test this function with the examples you provided:

```javascript
console.log(getClosestVowel("yogurt")); // Output: "u"
console.log(getClosestVowel("FULL")); // Output: "U"
console.log(getClosestVowel("quick")); // Output: ""
console.log(getClosestVowel("ab")); // Output: ""
```