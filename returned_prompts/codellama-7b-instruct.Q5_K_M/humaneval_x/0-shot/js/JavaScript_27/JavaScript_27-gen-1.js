/* For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
  >>> flipCase('Hello')
  'hELLO'
  */
const flipCase = (string) => {
  return string.split('').map((char, index) => {
    if (char.match(/[a-z]/)) {
      return char.toUpperCase()
    } else if (char.match(/[A-Z]/)) {
      return char.toLowerCase()
    } else {
      return char
    }
  }).join('')
}

