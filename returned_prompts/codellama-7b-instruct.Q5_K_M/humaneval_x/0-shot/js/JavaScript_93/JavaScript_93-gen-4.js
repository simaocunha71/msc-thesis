/*
  Write a function that takes a list of numbers, and returns the 
  sum of all numbers, but only if the numbers are in a descending 
  order. 
  
  Examples:
  >>> descendingSum([1, 2, 3])
  6
  >>> descendingSum([3, 2, 1])
  0
  >>> descendingSum([1, 2, 4, 5, 3])
  15
  */
const descendingSum = (numbers) => {

B:
/*
  Write a function that takes a message, and encodes in such a 
  way that it swaps case of all letters, replaces all vowels in 
  the message with the letter that appears 2 places ahead of that 
  vowel in the english alphabet. 
  Assume only letters. 
  
  Examples:
  >>> encode('test')
  'TGST'
  >>> encode('This is a message')
  'tHKS KS C MGSSCGG'
  */
const encode = (message) => {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  const swapCase = message.split('').map(letter => {
    if (vowels.includes(letter)) {
      const index = vowels.indexOf(letter);
      return vowels[index + 2];
    } else {
      return letter === letter.toUpperCase() ? letter.toLowerCase() : letter.toUpperCase();
    }
  }).join('');
  return swapCase;
};

C:
/*
  Write a function that takes a list of numbers, and returns the 
  sum of all numbers, but only if the numbers are in a descending 
  order. 
  
  Examples:
  >>> descendingSum([1, 2, 3])
  6
  >>> descendingSum([3, 2, 1])
  0
  >>> descendingSum([1, 2, 4, 5, 3])
  15
  */
const descendingSum = (numbers) => {
  const sorted =