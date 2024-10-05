  var result = [];
  var beats = 0;

  for (const c of music_string) {
    if (c == 'o') {
      beats = 4;
    } else if (c == '|') {
      if (beats == 4) {
        beats = 2;
      } else if (beats == 2) {
        beats = 1;
      }
    }
    result.push(beats);
  }

  return result;
}

