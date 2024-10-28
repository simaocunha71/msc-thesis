```js
const wordsInSentence = (sentence) => {
    const isPrime = (num) => {
        if (num < 2) return false;
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return true;
    };

    return sentence
        .split(' ')
        .filter((word) => isPrime(word.length))
        .join(' ');
};
```
