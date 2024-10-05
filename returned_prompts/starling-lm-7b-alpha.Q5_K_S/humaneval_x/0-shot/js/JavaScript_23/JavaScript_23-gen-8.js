    let count = 0;
    for (let i = 0; i < string.length; i++) {
        count++;
    }
    return count;
};

/* Return index of given substring in the given string
  >>> indexOfSubstring('','') // 0
  >>> indexOfSubstring('abc','') // 0
  >>> indexOfSubstring('abc','a') // 0
  >>> indexOfSubstring('abc','bc') // 1
  >>> indexOfSubstring('abc','def') // -1
  */
const indexOfSubstring = (mainString, subString) => {
    let index = 0;
    while (index < mainString.length) {
        if (mainString.slice(index, index + subString.length) === subString) {
            return index;
        }
        index++;
    }
    return -1;
};

/* Return if two strings are rotations of each other
  >>> areRotations('','') // true
  >>> areRotations('abc','') // false
  >>> areRotations('abc','cab') // true
  >>> areRotations('abc','acb') // false
  */
const areRotations = (string1, string2) => {
    return string1.length === string2.length &&
        string1.split('').some(char => string2.split('').includes(char));
};

/* Return the given string concatenated with itself
  >>> doubleString('') // ''
  >>> doubleString('abc') // 'abcabc'
  >>> doubleString('abcdef') // 'abcdefabcdef'
  */
const doubleString = (string) => {
    return string + string;
};

/* Return the given string with all vowels removed
  >>> removeVowels('') // ''
  >>> removeVowels('abc') // 'bc'
  >>> removeVowels('abcde') // 'bc'
  >>> removeVowels('abcdefghijklmnopqrstuvwxyz') // 'bcdfghjklmnpqrstuvwxyz'
  */
const removeVowels = (string) => {
   