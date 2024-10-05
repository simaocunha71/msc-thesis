    let consonantArray = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];
    let words = s.split(" ");
    let result = [];

    words.forEach(word => {
        let count = 0;
        for(let i = 0; i < word.length; i++) {
            if(consonantArray.includes(word[i])) {
                count++;
            }
        }
        if(count == n) {
            result.push(word);
        }
    });

    return result;
};

selectWords("Mary had a little lamb", 4);
selectWords("Mary had a little lamb", 3);
selectWords("simple white space", 2);
selectWords("Hello world", 4);
selectWords("Uncle sam", 3);
*/

Ans:
To solve this problem, we can follow these steps:

1. Initialize an array called `consonantArray` which contains all the consonant letters.
2. Split the input string `s` into an array of words using the space character as the delimiter. Store the result in the `words` array.
3. Initialize an empty array called `result` to store the words that contain exactly `n` consonants.
4. Iterate over each word in the `words` array using the `forEach` method. For each word, perform the following steps:
   - Initialize a variable `count` to 0 to keep track of the number of consonants in the current word.
   - Iterate over each character in the word using a `for` loop. For each character, check if it is a consonant by using the `includes` method on the `consonantArray`. If it is a consonant, increment the `count` variable by 1.
   - After the inner loop finishes, check if the `count` variable is equal to the desired number of consonants `n`. If it is, push the word into the `result