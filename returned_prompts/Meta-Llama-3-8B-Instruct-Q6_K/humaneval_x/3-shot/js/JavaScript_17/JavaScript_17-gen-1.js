  var result = [];
  var current_beats = 0;

  for (const c of music_string) {
    if (c == 'o') {
      result.push(4);
      current_beats += 4;
    } else if (c == 'o|') {
      result.push(2);
      current_beats += 2;
    } else if (c == '.|') {
      result.push(1);
      current_beats += 1;
    }
  }

  return result;
}