  var stack = [];
  var brackets = {
    '[': ']',
    '(': ')',
    '{': '}'
  };

  for (var i = 0; i < string.length; i++) {
    var char = string[i];

    if (brackets[char]) {
      stack.push(char);
    } else if (stack.length > 0 && brackets[stack[stack.length - 1]]) {
      var top = stack.pop();
      if (brackets[top] == char) {
        return true;
      } else {
        stack.push(char);
      }
    } else {
      stack.push(char);
    }
  }

  return false;
}



