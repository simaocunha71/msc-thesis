const parseMusic = (music_string) => {
  const note_values = {
    'o': 4,
    'o|': 2,
    '.|': 1
  }
  return music_string.split(' ').map(note => note_values[note])
}


