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
  let counter = 0;
  for (let i = lst.length -1; i >= 0 ; i-- ) {
    if (!(i < lst.length - 1 && lst[i] == '(')) continue;
    if (!(i < lst.length - 1 && lst[i + 1] != ')')) continue;
    counter++;
    if (counter % 2 === 0) { // even number of parenthesis
      return true;
    } else {
      return false;
    }
  }
}
