  let result = [];
  let current_note = music_string[0];
  let current_beat = 0;

  for (let i = 0; i < music_string.length; i++) {
    if (music_string[i] == '|') {
      result.push(current_beat);
      current_beat = 0;
      current_note = music_string[i + 1];
    } else {
      current_beat += 1;
    }
  }

  result.push(current_beat);

  return result;
}



