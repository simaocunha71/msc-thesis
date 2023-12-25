/* Input to this function is a string representing musical notes in a special ASCII format.
  Your task is to parse this string and return list of integers corresponding to how many beats does each
  not last.

  Here is a legend:
  'o' - whole note, lasts four beats
  'o|' - half note, lasts two beats
  '.|' - quater note, lasts one beat

  >>> parseMusic('o o| .| o| o| .| .| .| .| o o')
  [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
  */
const parseMusic = (music_string) => {
  const beats_array = [];
  for (let i = 0; i < music_string.length; ++i) {
    switch (music_string[i]) {
      case 'o': {
        if (!beat(1, beats_array)) { return []; }
        break;
      }
      case '.|': {
        if (!beat(2, beats_array)) { return []; }
        break;
      }
      case 'o|': {
        if (!beat(3, beats_array)) { return []; }
        break;
      }
      default: {
        throw new Error('Invalid note');
      }
    }
  }

  return [...Array(music_string.length)].map((_, i) => parseFloat(beats_array[i]));
};
