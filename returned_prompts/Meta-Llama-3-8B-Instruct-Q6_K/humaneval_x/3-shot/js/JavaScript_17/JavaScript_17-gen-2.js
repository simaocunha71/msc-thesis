  var result = [];
  var beats = 0;

  for (const c of music_string) {
    if (c == 'o') {
      beats += 4;
      result.push(4);
    } else if (c == 'o|') {
      beats += 2;
      result.push(2);
    } else if (c == '.|') {
      beats += 1;
      result.push(1);
    }
  }

  return result;
}