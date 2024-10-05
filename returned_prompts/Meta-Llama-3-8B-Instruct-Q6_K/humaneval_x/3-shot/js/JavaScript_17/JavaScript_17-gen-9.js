  var result = [];
  var current_note = '';
  var current_beats = 0;

  for (const c of music_string) {
    if (c == 'o') {
      current_note += c;
      current_beats += 4;
    } else if (c == '|') {
      if (current_note.length > 0) {
        if (current_note[current_note.length - 1] == 'o') {
          current_beats -= 4;
        } else {
          current_beats -= 2;
        }
        current_note = '';
      }
    } else if (c == '.') {
      if (current_note.length > 0) {
        if (current_note[current_note.length - 1] == 'o') {
          current_beats -= 4;
        } else {
          current_beats -= 2;
        }
        current_note = '';
        current_beats -= 1;
      }
    }
  }

  result.push(current_beats);
  return result;
}