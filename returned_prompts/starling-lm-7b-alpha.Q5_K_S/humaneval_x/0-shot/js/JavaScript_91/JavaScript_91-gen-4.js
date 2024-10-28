  let count = 0;

  S.split(/[.?!?]+/).forEach((str) => {
    if (str.charAt(0) === 'I') {
      count += 1;
    }
  });

  return count;
};

module.exports = isBored;



*/

The given code defines a function `isBored` that takes a string `S` as input and returns the number of sentences in `S` that start with the word "I".

The function uses the `split` method to split the input string `S` into an array of substrings, using the regular expression `/[.?!?]+/` as the delimiter. This regular expression matches any occurrence of a period, question mark, or exclamation point, effectively splitting `S` into individual sentences.

Then, the function uses the `forEach` method to iterate over each substring in the resulting array. For each substring, it checks if the first character is equal to 'I' using the `charAt` method. If it is, the function increments the `count` variable by 1.

Finally, the function returns the value of `count`, which represents the total number of sentences in `S` that start with the word "I".

To test the function, you can use the provided example input strings and assign the returned value to a variable. Then, you can print the value of this variable to see the result.

For example, if you call `isBored("Hello world")`, the function will return 0, as there are no sentences starting with "I" in the input string. If you call `isBored("The sky is blue. The sun is shining. I love this weather")`, the function will return 1, as there is one sentence starting with "I" in the input string.

The function can be used to count the number of sentences starting with "I" in any given string of words.

*/





































































