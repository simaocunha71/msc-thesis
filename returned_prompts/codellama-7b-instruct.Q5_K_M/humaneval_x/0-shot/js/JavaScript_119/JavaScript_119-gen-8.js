/* You are given a list of two strings, both strings consist of open
  parentheses '(' or close parentheses ')' only.
  Your job is to check if it is possible to concatenate the two strings in
  some order, that the resulting string will be good.
  A string S is considered to be good if and only if all parentheses in S
  are balanced. For example: the string '(())()' is good, while the string
  '())' is not.
  Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
  Examples:
  matchParens(['()(', ')']) == 'Yes'
  matchParens([')', ')']) == 'No'
  */
const matchParens = (lst) => {
  let stack = [];
  let result = true;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] === '(') stack.push(lst[i]);
    if (lst[i] === ')') {
      if (stack.length > 0) {
        stack.pop();
      } else {
        result = false;
        break;
      }
    }
  }
  if (stack.length === 0) result = true;
  else result = false;
  return result ? 'Yes' : 'No';
};

// OR

const matchParens = (lst) => {
  const stack = [];
  for (const char of lst) {
    if (char === '(') stack.push(char);
    if (char === ')') {
      if (stack.length > 0) stack.pop();
      else return 'No';
    }
  }
  return stack.length === 0 ? 'Yes' : 'No';
};
