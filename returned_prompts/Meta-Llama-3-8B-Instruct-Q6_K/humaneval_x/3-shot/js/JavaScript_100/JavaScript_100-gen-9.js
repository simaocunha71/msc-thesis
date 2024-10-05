  var result = [];
  var current_type = n % 2 == 0 ? 'even' : 'odd';
  var current_value = n;

  for (let i = 0; i < n; i++) {
    result.push(current_value);
    if (current_type == 'even') {
      current_value += 2;
    } else {
      current_value += 1;
    }
    current_type = current_type == 'even' ? 'odd' : 'even';
  }

  return result;
}