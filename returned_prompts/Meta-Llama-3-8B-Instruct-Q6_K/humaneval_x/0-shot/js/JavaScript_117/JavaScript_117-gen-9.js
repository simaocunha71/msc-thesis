Here is the solution in JavaScript:

```javascript
function selectWords(s, n) {
    let words = s.split(' ');
    let result = [];

    for (let word of words) {
        let consonants = 0;
        for (let char of word) {
            if (!['a', 'e', 'i', 'o', 'u'].includes(char.toLowerCase())) {
                consonants++;
            }
        }
        if (consonants === n) {
            result.push(word);
        }
    }

    return result;
}
```

In this solution, we first split the input string `s` into an array of words using the `split` method. Then, we iterate over each word and count the number of consonants using a second loop. We check if the number of consonants matches the input `n`, and if it does, we add the word to the result array. Finally, we return the result array. This function works as expected for the given examples.