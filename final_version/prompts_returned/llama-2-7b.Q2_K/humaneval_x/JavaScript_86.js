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
    let rtnStr = '';
    for(let i=0; i<s.length; i++){
        // if the character is already in correct order, then stop the loop
        if((i + 1) < s.length && s[i] <= s[i+1]) break;
        rtnStr = s[i]+rtnStr+' ';
    }
    return rtnStr;
}
console.log(antiShuffle('Hi')) // output 'Hi'
console.log(antiShuffle('hello')) // output 'ehllo'
console.log(antiShuffle('Hello World!!!')) // output 'Hello !!!Wdlor'