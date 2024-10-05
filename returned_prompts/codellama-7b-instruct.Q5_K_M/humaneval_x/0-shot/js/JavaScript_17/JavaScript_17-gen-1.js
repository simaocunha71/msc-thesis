
const parseMusic = (music_string) => {
  const beats = {
    'o': 4,
    'o|': 2,
    '.|': 1
  };
  return music_string.split('').map(ch => beats[ch]);
};
