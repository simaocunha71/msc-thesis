const parseMusic = (music_string) => {
  const whole_note = 4;
  const half_note = 2;
  const quarter_note = 1;
  const beat_map = {
    'o': whole_note,
    'o|': half_note,
    '.|': quarter_note
  };
  return music_string.split('|').map(beat => beat.split('').reduce((acc, curr) => acc * beat_map[curr], 1));
};
