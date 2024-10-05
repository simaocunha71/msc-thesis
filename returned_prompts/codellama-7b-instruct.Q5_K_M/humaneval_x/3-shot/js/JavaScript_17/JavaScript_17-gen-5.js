  var result = [];

  for (var i = 0; i < music_string.length; i++) {
    if (music_string[i] == 'o') {
      result.push(4);
    } else if (music_string[i] == '|') {
      if (music_string[i + 1] == 'o') {
        result.push(2);
      } else {
        result.push(1);
      }
    }
  }

  return result;
}



