  let array = [];
  while (a <= b) {
    let string = a.toString();
    for (let i = 0; i < string.length; i++) {
      if (string[i] % 2 === 0) {
        array.push(string[i]);
      }
    }
    a++;
  }
  return array.sort((a, b) => a - b);
};

console.log(generateIntegers(2, 8)); // [2, 4, 6, 8]
console.log(generateIntegers(8, 2)); // [2, 4, 6, 8]
console.log(generateIntegers(10, 14)); // []

*/

/*
In this kata you have to create a function that takes a string and a list of basic words. Your function must return a new string in which every word in the original string is replaced with the corresponding word in the list.

For example:

replace_words("This is a test", ["This", "That"]) will return "That is a test".

In the example above, the word "This" has been replaced by the word "That".

Notes:

    The original string and the list of words will never be empty.
    The original string will only contain English alphanumeric characters.
    Words in the string are separated by a single space.
    The list of words will only contain English alphanumeric characters.
    Words in the list are separated by a single space.


[Extras]

    Add a unit test to verify your code.
*/

const replace_words = (str, list) => {
  let words = str.split(' ');
  let new_words = [];
  for (let i = 0; i < words.length; i++) {
    if (list.includes(words[i])) {
      new_words.push(list.indexOf(words[i]));
    } else {
      new_words.push(words[i]);
    }
  }
  return new_words.join(' ');
};

console.log(replace_words("This is a test", ["This