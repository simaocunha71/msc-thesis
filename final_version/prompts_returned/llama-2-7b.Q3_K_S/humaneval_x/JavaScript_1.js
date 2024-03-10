/* Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
  separate those group into separate strings and return the list of those.
  Separate groups are balanced (each open brace is properly closed) and not nested within each other
  Ignore any spaces in the input string.
  >>> separateParenGroups('( ) (( )) (( )( ))')
  ['()', '(())', '(()())']
  */
const separateParenGroups = (paren_string) => {
  let strArr = paren_string.split(")"); // we split paren string into an array of strings

  const output = [];

  for (let index = 0; index < strArr.length - 1; index++) { // loop through the arrays elements
    if (strArr[index] === strArr[index + 1]) { // if current array element is equal to next elements, add it to output
      output.push(strArr[index]);
    } else { // other case: add a empty string between the two
      let end_of_array = strArr[index]; // set index+1 to last element (including itself)
      if (end_of_array === '') { // if we have an empty array, add an empty array to output
        output.push('');
      } else { // otherwise: add our current input string to the output list
        output.push(strArr[index]);
      }
    }
  }

  return output;
};