  var result = [];
  var current_duration = 0;

  for (const c of music_string) {
    if (c == 'o') {
      result.push(4);
    } else if (c == '|') {
      current_duration = 2;
    } else if (c == '.') {
      current_duration = 1;
    }
  }

  return result;
}



