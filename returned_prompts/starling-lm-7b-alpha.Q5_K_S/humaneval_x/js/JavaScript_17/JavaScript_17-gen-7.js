  let result = [];
  let curr = '';
  for (let c of music_string) {
    if (c == '|') {
      if (curr == 'o') {
        result.push(4);
      } else if (curr == 'o|') {
        result.push(2);
      } else if (curr == '.|') {
        result.push(1);
      }
      curr = '';
    } else {
      curr += c;
    }
  }
  if (curr) {
    if (curr == 'o') {
      result.push(4);
    } else if (curr == 'o|') {
      result.push(2);
    } else if (curr == '.|') {
      result.push(1);
    }
  }

  return result;
}



