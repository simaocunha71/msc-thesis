  const notes = {
    'o': 4,
    'o|': 2,
    '.': 1
  };

  let result = [];
  let note = '';
  for (const c of music_string) {
    if (notes[c]) {
      result.push(notes[c]);
      note = '';
    } else {
      note += c;
    }
  }

  return result;
}



