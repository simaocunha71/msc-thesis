/*
  Write a function that takes a string and returns an ordered version of it.
  Ordered version of string, is a string where all words (separated by space)
  are replaced by a new word where all the characters arranged in
  ascending order based on ascii value.
  Note: You should keep the order of words and blank spaces in the sentence.

  For example:
  antiShuffle('Hi') returns 'Hi'
  antiShuffle('hello') returns 'ehllo'
  antiShuffle('Hello World!!!') returns 'Hello !!!Wdlor'
  */
const antiShuffle = (s) => {
  const regex = /[a-z]/g;

  return s
    .replace(regex, (x) => {
      let counter = 0; // keep the count of each alphabets in string
      let alphabets = []; // array to hold all alphabets from string
      x.split('').forEach((ele) => {
        if (!counter || ele > counter) {
          counter++;
        } else {
          alphabets.push(ele);
        }
      });
      return alphabets.join(``);
    })
    .replace(/ /g, ''); // remove all spaces in string
};

// 1.
console.log(antiShuffle('Hi'));
/*
"Hi"
*/

// 2.
console.log(antiShuffle('hello'));
/*
"ehllo"
*/

// 3.
console.log(antiShuffle('Hello World!!!'));
/*
"Hello !!!Wdlor"