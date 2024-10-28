  var result = [];
  var current_beat = 0;

  for (const c of music_string) {
    if (c == 'o') {
      current_beat = 4;
    } else if (c == '|') {
      current_beat = 2;
    } else if (c == '.') {
      current_beat = 1;
    }
    result.push(current_beat);
  }

  return result;
}