  var result = [];
  for (let i = 0; i < music_string.length; i++) {
    if (music_string[i] == 'o') {
      result.push(4);
    } else if (music_string[i] == 'o|') {
      result.push(2);
    } else if (music_string[i] == '.|') {
      result.push(1);
    }
  }
  return result;
}