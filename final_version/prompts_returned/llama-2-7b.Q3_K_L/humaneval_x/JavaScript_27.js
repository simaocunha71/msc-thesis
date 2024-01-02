/* For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
  >>> flipCase('Hello')
  'hELLO'
  */
const flipCase = (string) => {
  return string.split("").map((letter) => {
    let newValue;
    if (letter.toUpperCase() === letter) { // Upper case
      newValue = letter.toLowerCase();
    } else {
      newValue = letter.toUpperCase();
    }
    return newValue;
  }).join("");
};
console.log(flipCase('Hello'));
