    const arr = sentence.split(' ');
    let ans = '';
    for (let i = 0; i < arr.length; i++) {
        if (isPrime(arr[i].length)) {
            ans += arr[i] + ' ';
        }
    }
    return ans.trim();
};

function isPrime(n) {
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if (n % 2 === 0 || n % 3 === 0) {
        return false;
    }
    for (let i = 5; i * i <= n; i = i + 6) {
        if (n % i === 0 || n % (i + 2) === 0) {
            return false;
        }
    }
    return true;
}

console.log(wordsInSentence('This is a test')); // "is"
console.log(wordsInSentence('lets go for swimming')); // "go for"

*/

// Time Complexity: O(nlogn), where n is the total number of characters in the sentence
// Space Complexity: O(1)

// Optimized Solution
const wordsInSentence = (sentence) => {
    const arr = sentence.split(' ');
    let ans = '';
    for (let i = 0; i < arr.length; i++) {
        if (isPrime(arr[i].length)) {
            ans += arr[i] + ' ';
        }
    }
    return ans.trim();
};

function isPrime(n) {
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if (n % 2 === 0 || n % 3 === 0) {
        return false;
    }
    for (let i = 5; i * i <= n; i = i + 6) {
        if (n % i === 0 || n % (i + 2) === 