/*
  Create a function that takes a string as input which contains only square brackets.
  The function should return true if and only if there is a valid subsequence of brackets
  where at least one bracket in the subsequence is nested.
  isNested('[[]]') ➞ true
  isNested('[]]]]]]][[[[[]') ➞ false
  isNested('[][]') ➞ false
  isNested('[]') ➞ false
  isNested('[[][]]') ➞ true
  isNested('[[]][[') ➞ true
  */
const isNested = (string) => {
  const bracketPattern = /[[\]]/g; // regex object that will match square brackets
  let openingBracketsCount = bracketPattern.exec(string).length; // variable to store the number of open brackets in string
  if (!openingBracketsCount) return false; // condition for returning a value when there are no matching bracket
  
  const closingBracketsCount = bracketPattern.exec(string)[0].replace(/^[\]|\]$/g, '').length; // variable to store the number of close brackets in string (matched by regex)
  if (!closingBracketsCount) return false; // condition for returning a value when there are no matching bracket

  let startIndex = 0; // variable that will store the current index in string
  while(startIndex < openingBracketsCount){ // loop to check if the brackets can be nested as per user input
    const endIndex = closingBracketsCount - 1; // end index which is 1 less than closing brackets count
    
    let substring = string.slice(startIndex, endIndex + 1); // substring starts from start-index to the end-index in the original string (start index excluded)
  	if (!substring || typeof substring === 'undefined') return false; // condition for returning a value when there are no matching brackets
    if(!substring.match(/[][[]/)) { return false; }
  }
  return true;
};