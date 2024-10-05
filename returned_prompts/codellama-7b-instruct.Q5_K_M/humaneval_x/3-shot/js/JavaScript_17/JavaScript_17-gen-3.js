  var result = [];
  var current_string = '';
  var current_beats = 0;

  for (const c of music_string) {
    if (c == 'o') {
      current_string += c;
      current_beats += 4;
    } else if (c == '|') {
      result.push(current_beats);
      current_string += c;
      current_beats = 0;
    } else if (c == '.') {
      current_string += c;
      current_beats += 1;
    }
  }

  if (current_string != '') {
    result.push(current_beats);
  }

  return result;
}



