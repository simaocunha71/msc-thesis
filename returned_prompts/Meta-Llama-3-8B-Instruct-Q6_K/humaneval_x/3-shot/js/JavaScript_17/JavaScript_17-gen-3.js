  var result = [];
  var current_beat = 0;
  var current_note = '';

  for (const c of music_string) {
    if (c == 'o') {
      current_beat += 4;
    } else if (c == '|') {
      if (current_note.length > 0) {
        result.push(current_beat);
        current_beat = 0;
        current_note = '';
      }
    } else if (c == '.') {
      if (current_note.length > 0) {
        result.push(current_beat);
        current_beat = 0;
        current_note = '';
      } else {
        current_beat += 1;
      }
    } else {
      if (current_note.length > 0) {
        result.push(current_beat);
        current_beat = 0;
        current_note = '';
      }
      current_note += c;
    }
  }
  if (current_note.length > 0) {
    result.push(current_beat);
  }
  return result;
}  } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } }