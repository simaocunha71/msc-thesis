  var result = [];
  var beats = 0;

  for (const c of music_string) {
    if (c == 'o') {
      beats += 4;
    } else if (c == 'o|') {
      beats += 2;
    } else if (c == '.|') {
      beats += 1;
    }
    result.push(beats);
  }

  return result;
}