/* For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
  >>> flipCase('Hello')
  'hELLO'
  */
const flipCase = (string) => {
  return string.toLowerCase().split('').map((letter)=>!0===letter? letter.toUpperCase():letter).join('');
}
console.log(flipCase("Hello")); //hELLO
