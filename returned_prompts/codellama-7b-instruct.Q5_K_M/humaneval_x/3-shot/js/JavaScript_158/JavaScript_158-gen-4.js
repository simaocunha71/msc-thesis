  var max_string = '';
  var max_length = 0;

  for (const word of words) {
    if (word.length > max_length) {
      max_length = word.length;
      max_string = word;
    } else if (word.length == max_length) {
      if (word < max_string) {
        max_string = word;
      }
    }
  }

  return max_string;
}



