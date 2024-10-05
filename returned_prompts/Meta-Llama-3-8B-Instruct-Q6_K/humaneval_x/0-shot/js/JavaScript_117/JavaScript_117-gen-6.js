```javascript
function selectWords(s, n) {
    const consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    const words = s.split(" ");
    const result = [];

    for (const word of words) {
        let count = 0;
        for (const char of word) {
            if (consonants.includes(char)) {
                count++;
            }
        }
        if (count === n) {
            result.push(word);
        }
    }

    return result;
}
```



The function `selectWords` takes a string `s` and a natural number `n` as inputs, and returns a list of all words from string `s` that contain exactly `n` consonants.

Here is a step-by-step explanation of how the function works:

1. It defines a string `consonants` that contains all the consonants in both uppercase and lowercase letters.
2. It splits the input string `s` into individual words using the `split` method with a space character as the separator.
3. It initializes an empty list `result` to store the words that contain exactly `n` consonants.
4. It iterates over each word in the `words` array.
5. For each word, it initializes a counter `count` to 0.
6. It iterates over each character `char` in the word.
7. If the character is a consonant (i.e., it is included in the `consonants` string), it increments the `count` by 1.
8. After iterating over all characters in the word, it checks if the `count` is equal to `n`. If it is, it adds the word to the `result` list.
9. Finally, it returns the `result` list.

The function is case-insensitive, meaning it treats uppercase and lowercase consonants as the same. It also ignores spaces and punctuation marks in the input string.

Here is an example of how the function can be used:

```javascript
console.log(selectWords("Mary had a little lamb", 4)); // Output: ["little"]
console.log(selectWords("Mary had a little lamb", 3)); // Output: ["Mary"]
console.log(selectWords("simple white space", 2)); // Output: []
console.log(selectWords("Hello world", 4)); // Output: ["world"]
console.log(selectWords("Uncle sam", 3)); // Output: