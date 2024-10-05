  let beats = [];
  let current_note = '';
  let current_beats = 0;

  for (const c of music_string) {
    if (c == 'o' || c == 'o|') {
      if (current_note === '') {
        current_note = c;
        current_beats = c === 'o' ? 4 : 2;
      } else {
        beats.push(current_beats);
        current_note = c;
        current_beats = c === 'o' ? 4 : 2;
      }
    } else if (c == '.' || c == '.|') {
      if (current_note !== '') {
        beats.push(current_beats);
        current_note = '';
        current_beats = c === '.' ? 1 : 0.5;
      }
    }
  }

  if (current_note !== '') {
    beats.push(current_beats);
  }

  return beats;
}