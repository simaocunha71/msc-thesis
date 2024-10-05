  var result = [];
  var current_beat = 0;

  for (const c of music_string) {
    if (c == 'o') {
      current_beat = 4;
    } else if (c == '|') {
      if (music_string[music_string.indexOf(c) - 1] == 'o') {
        current_beat = 2;
      } else {
        current_beat = 1;
      }
    }

    result.push(current_beat);
  }

  return result;
}