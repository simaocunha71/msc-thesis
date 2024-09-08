  const notes = ['o', 'o|', '.', '|'];
  const beats = [4, 2, 1, 1];
  let result = [];
  let current_note = 0;

  for (const c of music_string) {
    if (notes.includes(c)) {
      result.push(beats[notes.indexOf(current_note)]);
      current_note = c;
    } else if (c == '|') {
      current_note = notes[notes.indexOf(current_note) + 1];
    }
  }

  return result;
}



