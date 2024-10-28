  var result = [];
  var current_note = '';
  var current_duration = 0;

  for (const c of music_string) {
    if (c == 'o') {
      if (current_note != '') {
        result.push(current_duration);
      }
      current_duration = 4;
      current_note = 'o';
    } else if (c == '|') {
      if (current_note == 'o') {
        current_duration = 2;
      } else if (current_note == '.') {
        current_duration = 1;
      } else {
        current_duration = 1;
      }
    } else {
      current_note = c;
    }
  }

  result.push(current_duration);

  return result;
}
