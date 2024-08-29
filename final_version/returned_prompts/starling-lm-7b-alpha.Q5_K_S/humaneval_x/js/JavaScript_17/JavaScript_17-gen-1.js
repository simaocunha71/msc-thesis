  var result = [];
  for (const c of music_string) {
    if (c == 'o') {
      result.push(4);
    } else if (c == 'o|') {
      result.push(2);
    } else if (c == '.|') {
      result.push(1);
    }
  }
  return result;
}



