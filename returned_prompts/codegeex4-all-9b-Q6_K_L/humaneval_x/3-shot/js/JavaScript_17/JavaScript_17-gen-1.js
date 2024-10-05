  var result = [];
  var current_beat = 0;

  for (const c of music_string) {
    if (c == 'o') {
      current_beat += 4;
      result.push(4);
    } else if (c == 'o|') {
      current_beat += 2;
      result.push(2);
    } else if (c == '.|') {
      current_beat += 1;
      result.push(1);
    }
  }

  return result;
}

