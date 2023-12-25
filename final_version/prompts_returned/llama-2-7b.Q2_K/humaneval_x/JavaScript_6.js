/* Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
  For each of the group, output the deepest level of nesting of parentheses.
  E.g. (()()) has maximum two levels of nesting while ((())) has three.

  >>> parseNestedParens('(()()) ((())) () ((())()())')
  [2, 3, 1, 3]
  */
const parseNestedParens = (paren_string) => {
  const result = [];
  let currentGroup = null; // the beginning of the group
  for (var i = 0; i < paren_string.length; i++) {
    if ((paren_string[i] === '(' || paren_string[i] === ')') &&
      (currentGroup == null)) { // starting a new group?
        currentGroup = i - 1; // the position of the last character in the group
    } else if (paren_string[i] === ')') { // at the end of a group
      if (result.length > 0) {
        result[result.length-1].push(currentGroup); // add it to the list of groups
      }
      currentGroup = null; // start a new group
    } else if ((paren_string[i] === '(' || paren_string[i] === ')') && 
                   (currentGroup != null)) { // in the middle of a group
        console.log(`The position of '(' or ')' in currentGroup: ${currentGroup}`);
      } else if ((paren_string[i] === '{') || // on the end of a group but with an odd level number (for example, not enough parentheses)
                            (paren_string[i] === '}')) { // or in the middle without an even level number (e.g., '()')
          if (currentGroup == null){ // start a new one
            currentGroup = i - 1; // where this character is placed
          } else {
            result[result.length-1].push(currentGroup); // add it to the list of groups
            currentGroup = i - 1; // continue with the middle one, if any
          }
