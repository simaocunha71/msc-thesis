  var result = [];
  var music_string = music_string.split(' ');

  for (const note of music_string) {
    if (note == 'o') {
      result.push(4);
    } else if (note == 'o|') {
      result.push(2);
    } else if (note == '.|') {
      result.push(1);
    }
  }

  return result;
}