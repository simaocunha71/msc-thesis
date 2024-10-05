  var stack = [];
  var current_depth = 0;
  var current_start = 0;

  for (let i = 0; i < string.length; i++) {
    if (string[i] == '[') {
      current_depth += 1;
      if (current_depth == 1) {
        current_start = i;
      }
    } else if (string[i] == ']') {
      current_depth -= 1;
      if (current_depth == 0) {
        if (current_start != i) {
          return true;
        }
      }
    }
  }

  return false;
}

