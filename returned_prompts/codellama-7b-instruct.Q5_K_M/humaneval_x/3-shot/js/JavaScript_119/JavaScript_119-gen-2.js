  var stack = [];
  for (var i = 0; i < lst.length; i++) {
    if (lst[i] == '(') {
      stack.push('(');
    } else if (lst[i] == ')') {
      if (stack.length == 0) {
        return 'No';
      } else {
        stack.pop();
      }
    }
  }
  if (stack.length == 0) {
    return 'Yes';
  } else {
    return 'No';
  }
}



