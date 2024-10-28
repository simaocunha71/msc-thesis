
function check(s) {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') {
      count++;
    } else {
      if (count === 0) {
        return false;
      }
      count--;
    }
  }
  return count === 0;
}

return check(lst[0]) || check(lst[1]) || check(`${lst[0]}${lst[1]}`);

}

matchParens(['()(', ')']) // "Yes"
matchParens([')', ')']) // "No"






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














































































































































































