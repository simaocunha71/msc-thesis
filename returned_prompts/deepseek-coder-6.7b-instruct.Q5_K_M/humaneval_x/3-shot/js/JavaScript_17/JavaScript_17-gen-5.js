  var beats = { 'o': 4, 'o|': 2, '.|': 1 };
  return music_string.split(' ').map(note => beats[note]);
}



