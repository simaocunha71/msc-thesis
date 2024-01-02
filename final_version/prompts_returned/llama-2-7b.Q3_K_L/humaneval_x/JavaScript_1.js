/* Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
  separate those group into separate strings and return the list of those.
  Separate groups are balanced (each open brace is properly closed) and not nested within each other
  Ignore any spaces in the input string.
  >>> separateParenGroups('( ) (( )) (( )( ))')
  ['()', '(())', '(()())']
  */
const separateParenGroups = (paren_string) => {
  let openBrace = false;
  const result = [];
  
  for (let i = 0; i < paren_string.length - 1; i++) { //for loop for the string from index 0 to length -1 but not including the last character
    if (paren_string[i] === '(' && !openBrace) {
      result.push('()');
    } else if (paren_string[i] === ')') { //if it's a close parenthesis check that there is an open one in the previous index - 1, and if so then add to the results array
      if (!openBrace) result.push('()');
    } else if (paren_string[i] === '(' && openBrace) { //check for a close brace, if it's there then remove that from the previous index - 1 and add to the results array
      paren_string = paren_string.slice(0, i);
      result.push('()');
    } else if (paren_string[i] === ')') {
      openBrace = true; //open parenthesis has been found and will be closed next time a ')' is found
    } else if ((!openBrace && !paren_string.includes('()')) || (paren_string.lastIndexOf(',')) === 2) { //if the end of the string is reached then close all open parenthesis and add to result array - it's not balanced but it will be next time that a '(' or a ')' is found in the string
      if (openBrace && !paren_string.includes('()')) { //check for a closing brace, if there