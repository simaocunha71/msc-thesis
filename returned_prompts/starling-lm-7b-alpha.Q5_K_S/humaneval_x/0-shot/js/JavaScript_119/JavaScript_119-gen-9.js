
let a = lst[0];
let b = lst[1];

let count = 0;

for (let i = 0; i < a.length; i++) {
  if (a[i] === '(') {
    count++;
  } else {
    count--;
  }
  if (count < 0) {
    return 'No';
  }
}

count = 0;

for (let i = 0; i < b.length; i++) {
  if (b[i] === ')') {
    count++;
  } else {
    count--;
  }
  if (count < 0) {
    return 'No';
  }
}

if (count !== 0) {
  return 'No';
}

return 'Yes';

};

/* You are given a list of two strings, both strings consist of open
  parentheses '(' or close parentheses ')' only.
  Your job is to check if it is possible to concatenate the two strings in
  some order, that the resulting string will be good.
  A string S is considered to be good if and only if all parentheses in S
  are balanced. For example: the string '(())' is good, while the string
  '()(' is not.
  Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
  Examples:
  matchParens(['(', '())()']) == 'Yes'
  matchParens([')', ')']) == 'No'
*/











































































































































