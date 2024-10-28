  let parsed_notes = music_string.split(' ');
  let beats_list = [];
  for (let note of parsed_notes) {
    if (note === 'o') {
      beats_list.push(4);
    } else if (note === 'o|') {
      beats_list.push(2);
    } else if (note === '.|') {
      beats_list.push(1);
    } else {
      throw new Error('Invalid input');
    }
  }
  return beats_list;
}
