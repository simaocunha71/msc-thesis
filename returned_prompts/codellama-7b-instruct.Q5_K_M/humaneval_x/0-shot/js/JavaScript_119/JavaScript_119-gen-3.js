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

  const isBalanced = (str) => {
    const stack = [];
    for (const char of str) {
      if (char === '(') {
        stack.push(char);
      } else {
        if (stack.pop() !== '(') {
          return false;
        }
      }
    }
    return stack.length === 0;
  };

  let result = 'Yes';
  for (const str of lst) {
    if (!isBalanced(str)) {
      result = 'No';
      break;
    }
  }

  return result;
};


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

  const isBal