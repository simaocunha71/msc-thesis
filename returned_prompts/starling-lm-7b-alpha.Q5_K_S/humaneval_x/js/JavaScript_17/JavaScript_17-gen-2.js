  let result = [];
  let note = '';
  let beat = 0;
  for (const c of music_string) {
    if (c == 'o') {
      beat = 4;
    } else if (c == '|') {
      result.push(beat);
      beat = 0;
    } else {
      beat += 1;
    }
  }
  if (beat != 0) {
    result.push(beat);
  }

  return result;
}



