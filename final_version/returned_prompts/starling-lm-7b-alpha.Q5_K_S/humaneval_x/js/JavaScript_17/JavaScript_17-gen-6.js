  var result = [];
  var notes = music_string.split('|');
  for (const note of notes) {
    if (note == 'o') {
      result.push(4);
    } else if (note == '.') {
      result.push(1);
    } else {
      result.push(2);
    }
  }
  return result;
}



