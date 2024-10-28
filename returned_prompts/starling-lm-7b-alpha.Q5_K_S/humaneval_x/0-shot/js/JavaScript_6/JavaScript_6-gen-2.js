    let result = [];
    let current = 0;
    for (let i = 0; i < paren_string.length; i++) {
      if (paren_string[i] === '(') {
        current++;
      } else if (paren_string[i] === ')') {
        current--;
      } else if (paren_string[i] === ' ') {
        result.push(current);
      }
    }
    return result;
  };

parseNestedParens('(()()) ((())) () ((())()())');

/* Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
  For each of the group, output the deepest level of nesting of parentheses.
  E.g. (()()) has maximum two levels of nesting while ((())) has three.

  >>> parseNestedParens('(()()) ((())) () ((())()())')
  [2, 3, 1, 3]
  */
  // My solution

  const parseNestedParens = (str) => {
    let result = [];
    let current = 0;
    let open = 0;
    let close = 0;
    for(let i = 0; i < str.length; i++){
      if(str[i] == '(') {
        open++;
      } else if (str[i] == ')') {
        open--;
      } else if (str[i] == ' ') {
        result.push(open);
      }
    }
    return result;
  };

  parseNestedParens('(()()) ((())) () ((())()())');

  // Another solution

  const parseNestedParens = str => {
    const result = [];
    let max = 0;
    for (let i = 0; i < str.length; i++) {
      if (str[i] === '(') {
        max++;
      } else if (str[i] === ')') {
        max--;
      } else if (str[i] === ' ') {
        result.push(max);
      }
    }
   