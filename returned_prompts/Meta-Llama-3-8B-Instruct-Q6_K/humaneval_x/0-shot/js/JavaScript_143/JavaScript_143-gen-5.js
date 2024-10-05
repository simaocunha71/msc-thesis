```
function wordsInSentence(sentence) {
    const primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
    const words = sentence.split(' ');
    let result = '';
    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        if (primeNumbers.includes(word.length)) {
            result += word + ' ';
        }
    }
    return result.trim();
}
```

This function splits the input sentence into words, then iterates over each word. It checks if the length of the word is a prime number by checking if it exists in the `primeNumbers` array. If it is, the word is added to the result string. Finally, the function returns the result string with trailing spaces removed using the `trim()` method.

For example, if the input sentence is "This is a test", the function will return "is" because only "is" has a length that is a prime number (2). If the input sentence is "lets go for swimming", the function will return "go for" because both "go" and "for" have lengths that are prime numbers (3 and 3 respectively).