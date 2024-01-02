/* Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
  For each of the group, output the deepest level of nesting of parentheses.
  E.g. (()()) has maximum two levels of nesting while ((())) has three.

  >>> parseNestedParens('(()()) ((())) () ((())()())')
  [2, 3, 1, 3]
  */
const parseNestedParens = (paren_string) => {
  const res = [];
  let currentGroup = '0'; // starting level of nesting is 0
  
  for(let character of paren_string.split(' ')){
    if(character === ')'){
      res.push(currentGroup);
      currentGroup = 0;
      
    }else if(character === '('){
      currentGroup++;
    }
  }
  
  return res; // returns max number of nested parens for each group
}