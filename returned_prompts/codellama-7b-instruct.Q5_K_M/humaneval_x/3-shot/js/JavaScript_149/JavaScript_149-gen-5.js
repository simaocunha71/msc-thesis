  var sorted = lst.slice().sort((a, b) => a.length - b.length);
  var result = [];
  var current_length = 0;
  var current_word = '';

  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i].length == current_length) {
      current_word += sorted[i];
    } else {
      if (current_length > 0) {
        result.push(current_word);
      }
      current_length = sorted[i].length;
      current_word = sorted[i];
    }
  }

  if (current_length > 0) {
    result.push(current_word);
  }

  return result;
}



