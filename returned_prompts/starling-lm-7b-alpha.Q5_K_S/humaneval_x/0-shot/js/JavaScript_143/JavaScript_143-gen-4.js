    // Here, we can first split the sentence into an array of words
    let words = sentence.split(" ");

    // Next, we can loop through the array of words to filter out the words whose length is not prime
    let primeWords = words.filter(word => {
        for (let i = 2; i < word.length; i++) {
            if (word.length % i === 0) return false;
        }
        return true;
    });

    // Finally, we can return the joined array of words
    return primeWords.join(" ");
};

*/


/*
This problem is relatively straightforward. First, we split the input sentence into an array of words. Then, we use a for loop to iterate through each word in the array and check if its length is a prime number. If a word's length is not a prime number, we remove it from the array. Finally, we use the join function to join the remaining words in the array and return the result.

In the above solution, we first split the sentence into an array of words using the split function and store it in the variable "words". Then, we use the filter function to create a new array called "primeWords" that only includes the words whose lengths are prime numbers. In the filter function, we use a for loop to iterate through each word in the "words" array and check if its length is divisible by any number from 2 to the length of the word minus 1. If the length is divisible, we return false and continue checking the next word. If the length is not divisible by any number, we return true and add the word to the "primeWords" array. Finally, we use the join function to join all the words in the "primeWords" array and return the result.

The time complexity of this solution is O(n^2), where n is the length of the sentence. This is because we need to check each word's length for each word in the worst-case scenario. However, the space complexity is O(n), where n is the length of the sentence. This is because we need to store all the words in the "words" array and the "primeWords" array.
*/

*/














