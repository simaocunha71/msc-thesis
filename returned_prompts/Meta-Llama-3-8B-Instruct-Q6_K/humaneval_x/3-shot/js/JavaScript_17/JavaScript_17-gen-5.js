  var result = [];
  var beat = 0;

  for (const c of music_string) {
    if (c == 'o') {
      beat += 4;
      result.push(4);
    } else if (c == '|') {
      beat /= 2;
      result.push(beat);
    } else if (c == '.') {
      beat /= 2;
      result.push(beat);
      beat = Math.floor(beat);
    }
  }

  return result;
}