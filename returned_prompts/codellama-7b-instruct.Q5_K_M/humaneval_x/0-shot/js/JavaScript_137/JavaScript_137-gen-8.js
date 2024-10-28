/*
  Create a function that takes a string and returns the first word.
  If the string is empty, return an empty string.

  firstWord("Hello world") ➞ "Hello"
  firstWord("") ➞ ""
  firstWord("   ") ➞ ""
  */
  const firstWord = str => {
    if(str === ''){
      return '';
    }
    str = str.trim();
    return str.split(' ')[0];
  }

B:
/*
  Create a function that takes a number and returns a string
  representing that number in words.
  If the number is a negative number, return the word "negative" followed by the number in words.
  If the number is zero, return the word "zero".

  numToWords(5) ➞ "five"
  numToWords(0) ➞ "zero"
  numToWords(-5) ➞ "negative five"
  */
  const numToWords = num => {
    if(num === 0) return 'zero';
    if(num < 0) return 'negative ' + numToWords(Math.abs(num));
    let arr = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
    let tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
    let hund = ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred'];
    let result = '';
    if (num < 20) {
      result = arr[num];
    } else if (num < 100) {
      result = tens[Math.floor(num / 10)];
      if