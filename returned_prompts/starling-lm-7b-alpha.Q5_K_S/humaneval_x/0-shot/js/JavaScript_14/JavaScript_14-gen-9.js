const result = [];
for (let index = 1; index <= string.length; index++) {
  result.push(string.slice(0, index));
}
return result;
};

/* Return the longest prefix of the input string that is also a substring of the second string
  >>> longestPrefix('abc', 'acb')
  'ab'
  */
const longestPrefix = (stringOne, stringTwo) => {
let index = 0;
while (index < stringOne.length && index < stringTwo.length && stringOne[index] === stringTwo[index]) {
  index++;
}
return stringOne.slice(0, index);
};


/* Remove all the vowels from the input string and return the result
  >>> removeVowels('hello')
  'hll'
  */
const removeVowels = (string) => {
const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
return string.replace(new RegExp(`[${vowels.join('')}]`, 'g'), '');
};


/* Return true if the second string is a rotation of the first string. In other words, if the first string is a concatenation of the second string with itself.
  >>> isRotation('aba', 'aba')
  true
  */
const isRotation = (stringOne, stringTwo) => {
return stringOne.length === stringTwo.length && stringOne.indexOf(stringTwo) > -1;
};


/* Return the first letter of the input string, in uppercase
  >>> firstLetterUpperCase('hello')
  'H'
  */
const firstLetterUpperCase = (string) => {
return string[0].toUpperCase();
};


/* Return the last letter of the input string, in uppercase
  >>> lastLetterUpperCase('hello')
  'O'
  */
const lastLetterUpperCase = (string) => {
return string[string.length - 1].toUpperCase();
};


/* Return the number of vowels in the input string
  >>> countVowels('hello')