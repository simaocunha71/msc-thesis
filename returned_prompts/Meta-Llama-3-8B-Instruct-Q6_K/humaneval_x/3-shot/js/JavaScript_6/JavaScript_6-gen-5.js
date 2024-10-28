  var result = [];
  var current_string = [];
  var current_depth = 0;
  var stack = [];

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      stack.push(current_depth);
      current_string.push(c);
    } else if (c == ')') {
      current_depth -= 1;
      current_string.push(c);
      if (current_depth == 0) {
        result.push(stack.pop());
        current_string = [];
      }
    }
  }

  return result;
}  // end parseNestedParens function
// end of code
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
// end of file
// end of line
//