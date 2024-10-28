  var result = [];
  var current_beat = 0;
  for (const c of music_string) {
    if (c == 'o') {
      current_beat += 4;
    } else if (c == 'o|') {
      current_beat += 2;
    } else if (c == '.|') {
      current_beat += 1;
    }
  }
  result.push(current_beat);
  return result;
} // Not correct, this function should return all beats for the whole string, not just the last one.
// We need to keep track of all the beats and add them to the result array. Here is the corrected function:
const parseMusic = (music_string) => {
  var result = [];
  var current_beat = 0;
  for (const c of music_string) {
    if (c == 'o') {
      current_beat += 4;
      result.push(4);
    } else if (c == 'o|') {
      current_beat += 2;
      result.push(2);
    } else if (c == '.|') {
      current_beat += 1;
      result.push(1);
    }
  }
  return result;
}