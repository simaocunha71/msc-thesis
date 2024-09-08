  const notes = {
    "o": 4,
    "o|": 2,
    ".": 1
  };

  const result = [];

  for (const c of music_string) {
    result.push(notes[c]);
  }

  return result;
}



