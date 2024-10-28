
const notes = music_string.split("|");
const parsedNotes = [];
notes.forEach(note => {
  if (note === "o") {
    parsedNotes.push(4);
  } else if (note === "o|") {
    parsedNotes.push(2);
  } else if (note === ".|") {
    parsedNotes.push(1);
  }
});

return parsedNotes;
};

parseMusic('o o| .| o| o| o| .| .| .| .| o o');






/* Input to this function is a string representing musical notes in a special ASCII format.
  Your task is to parse this string and return list of integers corresponding to how many beats does each
  not last.

  Here is a legend:
  'o' - whole note, lasts four beats
  'o|' - half note, lasts two beats
  '.|' - quater note, lasts one beat

  >>> parseMusic('o o| .| o| o| o| .| .| .| .| o o')
  [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
  */














































































































































































































