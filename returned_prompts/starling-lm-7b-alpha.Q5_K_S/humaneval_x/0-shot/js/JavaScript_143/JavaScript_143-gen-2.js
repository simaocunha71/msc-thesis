    const words = sentence.split(" ");
    const result = [];
    for (let word of words) {
        if (isPrime(word.length)) {
            result.push(word);
        }
    }
    return result.join(" ");
};

function isPrime(n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 === 0 || n % 3 === 0) return false;
    for (let i = 5; i * i <= n; i += 6)
        if (n % i === 0 || n % (i + 2) === 0) return false;
    return true;
}

// Test
console.log(wordsInSentence("This is a test")); // "is"
console.log(wordsInSentence("lets go for swimming")); // "go for"
console.log(wordsInSentence("I am very happy")); // "am very"

*/


























/*

Explanation

Firstly, we need to check whether the length of the word is a prime number or not,
if the length of the word is a prime number, we add it to the result array;

Finally, we join the result array by a space to form the string, and return it;

Time Complexity: O(n)

*/

*/































































































































































