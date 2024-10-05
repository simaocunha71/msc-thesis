  var result = [];
  var current = '';
  for (const c of music_string) {
    if (c == ' ') {
      if (current) {
        result.push(current);
        current = '';
      }
    } else {
      current += c;
    }
  }
  if (current) {
    result.push(current);
  }

  var notes = {
    'o': 4,
    'o|': 2,
    '.|': 1
  };

  return result.map(n => notes[n]);
}