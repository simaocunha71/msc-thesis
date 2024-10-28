  var result = [];
  var current_length = 0;

  for (const c of music_string) {
    if (c == 'o') {
      current_length += 4;
    } else if (c == '|') {
      current_length += 2;
    } else if (c == '.') {
      current_length += 1;
    }
    result.push(current_length);
  }

  return result;
}



