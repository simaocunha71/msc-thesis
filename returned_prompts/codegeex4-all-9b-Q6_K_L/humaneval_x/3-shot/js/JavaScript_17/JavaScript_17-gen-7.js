  var result = [];
  var beats = 0;
  var current_beat = 0;

  for (const c of music_string) {
    if (c == 'o') {
      current_beat = 4;
    } else if (c == '|') {
      if (music_string[music_string.length - 1] == '|') {
        current_beat = 2;
      } else {
        current_beat = 1;
      }
    } else if (c == ' ') {
      continue;
    } else {
      return 'Invalid input';
    }

    beats += current_beat;
    result.push(beats);
  }

  return result;
}

