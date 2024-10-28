let open = 0;
for (let i = 0; i < lst[0].length; i++) {
  if (lst[0][i] === '(') {
    open++;
  } else {
    open--;
  }
  if (open < 0) {
    return 'No';
  }
}
if (open !== 0) {
  return 'No';
}

open = 0;
for (let i = 0; i < lst[1].length; i++) {
  if (lst[1][i] === '(') {
    open++;
  } else {
    open--;
  }
  if (open < 0) {
    return 'No';
  }
}
if (open !== 0) {
  return 'No';
}

return 'Yes';
};

matchParens(["(","()")]);


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
























































































































