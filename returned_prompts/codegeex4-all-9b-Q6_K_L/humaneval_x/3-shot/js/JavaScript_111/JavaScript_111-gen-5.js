  var result = {};
  var current_count = 0;
  var current_letter = '';

  for (var c of test) {
    if (c == ' ') {
      if (current_letter != '') {
        result[current_letter] = current_count;
      }
      current_letter = '';
      current_count = 0;
    } else {
      current_letter += c;
      current_count += 1;
    }
  }

  if (current_letter != '') {
    result[current_letter] = current_count;
  }

  return result;
}