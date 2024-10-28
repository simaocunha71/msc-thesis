
/* Check if in given list of numbers, are any two numbers closer to each other than
  given threshold.
  >>> hasCloseElements([1.0, 2.0, 3.0], 0.5)
  false
  >>> hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
  true
  */
const hasCloseElements = (numbers, threshold) => {

  // iterate over each number
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      // only compare each number to all other numbers
      if (i != j) {
        let distance = Math.abs(numbers[i] - numbers[j]);
        // if the distance is less than the threshold, return true
        if (distance < threshold) {
          return true;
        }
      }
    }
  }
  // if no numbers are close enough, return false
  return false;
}

/* Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
  separate those group into separate strings and return the list of those.
  Separate groups are balanced (each open brace is properly closed) and not nested within each other
  Ignore any spaces in the input string.
  >>> separateParenGroups('( ) (( )) (( )( ))')
  ['()', '(())', '(()())']
  */
const separateParenGroups = (paren_string) => {

  // create a list to store the groups
  var result = [];
  // create a list to store the current group
  var current_string = [];
  // create a variable to keep track of the current depth
  var current_depth = 0;

  // iterate over each character in the string
  for (const c of paren_string) {
    // if the character is an open parenthesis, increase the depth and add it to the current group
    if (c == '(') {
      current_depth += 1;
      current_string.push(c);
    // if the character is a close parenthesis, decrease the depth and add it to the current group
    } else if (c == ')') {
      current_depth -= 1