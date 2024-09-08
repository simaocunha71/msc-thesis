  let notes = [];
  let note = '';

  for (const c of music_string) {
    if (c == 'o' || c == 'o|' || c == '.|') {
      note += c;
    } else if (c == '|') {
      notes.push(note);
      note = '';
    }
  }

  return notes.map((note) => {
    if (note == 'o') {
      return 4;
    } else if (note == 'o|') {
      return 2;
    } else if (note == '.|') {
      return 1;
    } else {
      throw Error('Invalid note');
    }
  });
}



