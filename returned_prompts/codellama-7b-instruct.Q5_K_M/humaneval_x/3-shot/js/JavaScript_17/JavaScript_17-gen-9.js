  var result = [];
  var current_string = [];
  var current_depth = 0;

  for (const c of music_string) {
    if (c == 'o' || c == '|') {
      current_string.push(c);
    } else if (c == ' ') {
      if (current_string.join('') == 'o|') {
        result.push(2);
        current_string = [];
      } else if (current_string.join('') == '.|') {
        result.push(1);
        current_string = [];
      } else {
        result.push(4);
        current_string = [];
      }
    }
  }

  return result;
}



