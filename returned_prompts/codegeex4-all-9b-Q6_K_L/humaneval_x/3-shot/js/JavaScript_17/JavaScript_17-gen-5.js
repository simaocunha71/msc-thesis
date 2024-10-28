  var result = [];
  var beat_count = 0;

  for (const c of music_string) {
    if (c == 'o') {
      result.push(4);
    } else if (c == '|') {
      if (music_string[beat_count + 1] == '.') {
        result.push(1);
      } else {
        result.push(2);
      }
    }
    beat_count += 1;
  }

  return result;
}