  var beats_per_note = {'o': 4, 'o|': 2, '.|': 1};
  return music_string.split(' ').map(note => beats_per_note[note]);
}



