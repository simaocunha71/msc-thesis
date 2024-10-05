  var result = [];
  var current_prefix = '';

  for (const c of string) {
    current_prefix += c;
    result.push(current_prefix);
  }

  return result;
}



