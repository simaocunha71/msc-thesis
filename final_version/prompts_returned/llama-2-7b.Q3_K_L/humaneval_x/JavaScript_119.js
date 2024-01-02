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
  let len = lst[0].length;
  if(len < lst.reduce((a, b) => a + b.length)) {
    return "No"
  }
  
  // check left and right
  for(let i = 0; i < len - 1; ++i){
    const s = lst[i] + lst[i+1];
    if(!checkParens(s)) {
      return "No"
    }
  }
  
  return "Yes";
}

const checkParens = (str) => {
  // convert to array
  let arr = str.split("");
  
  // left
  for(let i = 0; i < arr.length - 1; ++i){
    if(arr[i] === '(' && arr[i+1] === ')') {
      return false;
    } else if(arr[i] === ')' && arr[i-1] === '(' ) {
      return true;
    }
  }
  
  // right
  for(let i = arr.length - 2, j = 0; i > j; ++i){
    if(arr[j] === '(' && arr[i+1] === ')') {
      return true;
    } else if(arr[j+1] === ')' && arr[i-2] ==='(') {
      return false;
    }