    let max = words[0];
    let maxLength = words[0].length;

    for (let i = 1; i < words.length; i++) {
        let word = words[i];
        let length = word.length;
        let unique = getUnique(word);
        if (unique > maxLength) {
            max = word;
            maxLength = length;
        }
        else if (unique === maxLength && word < max) {
            max = word;
        }
    }
    return max;
};

function getUnique(word) {
    let charSet = new Set();
    for (let i = 0; i < word.length; i++) {
        charSet.add(word[i]);
    }
    return charSet.size;
}

console.log(findMax(["name", "of", "string"]));
console.log(findMax(["name", "enam", "game"]));
console.log(findMax(["aaaaaaa", "bb", "cc"]));

*/

// This is the solution to the problem. O(n * m) time where n is the number of
// strings and m is the maximum length of a string. O(n) space for the charSet
// set.

// Note that the time complexity is not O(n * m * log m) as a naive approach
// might suggest. This is because the add operation on a set is O(1) on average
// (amortized), not O(log m).

// This solution works by iterating over all the strings and for each string
// finding the number of unique characters. It uses a set to store the unique
// characters because adding an element to a set is an O(1) operation on average
// (amortized). The maximum unique character count is stored along with the word
// that achieves it. If multiple strings have the maximum number of unique
// characters, the one that comes first in lexicographical order is chosen.

// The getUnique function is used to count the unique characters in a string. It
// iterates over each character in the string and adds it to a set. Since the add
// operation on a set is O(1)