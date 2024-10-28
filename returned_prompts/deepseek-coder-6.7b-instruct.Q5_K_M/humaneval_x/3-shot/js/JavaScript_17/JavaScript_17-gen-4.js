  var beats_per_note = {'o': 4, 'o|': 2, '.|': 1};
  var result = [];
  var current_beat = 0;

  for  (const note of music_string.split(' '))  {
    current_beat += beats_per_note[note];
    result.push(current_beat);
  }

  return result;
}



