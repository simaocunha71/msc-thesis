Here is the solution for the problem:

```javascript
const parseMusic = (music_string) => {
  const music_notes = music_string.split(' ');
  const note_beats = [];

  for (const note of music_notes) {
    switch (note) {
      case 'o':
        note_beats.push(4);
        break;
      case 'o|':
        note_beats.push(2);
        break;
      case '.|':
        note_beats.push(1);
        break;
      default:
        throw new Error(`Invalid music note: ${note}`);
    }
  }

  return note_beats;
};
```

This function splits the input string into individual notes, then iterates over each note. Depending on the note, it adds the corresponding number of beats to the `note_beats` array. Finally, it returns the `note_beats` array.

You can test this function with the example input you provided:

```javascript
console.log(parseMusic('o o| .| o| o| .| .| .| .| o o')); // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```  */  // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  */  // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  // [4, 2, 1, 