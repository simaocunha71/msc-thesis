```
const parseMusic = (music_string) => {
  const notes = music_string.split(' ');
  const beats = [];
  for (const note of notes) {
    switch (note) {
      case 'o': beats.push(4); break; // whole note
      case 'o|': beats.push(2); break; // half note
      case '.|': beats.push(1); break; // quater note
      default: throw new Error(`Invalid note: ${note}`);
    }
  }
  return beats;
};
```


This JavaScript function takes a string representing musical notes in a special ASCII format, parses it, and returns a list of integers corresponding to how many beats each note lasts.

The function first splits the input string into individual notes using the `split` method with a space character as the separator. It then iterates over each note and uses a `switch` statement to determine the number of beats the note lasts, based on the legend provided.

For example, if the input string is `'o o| .| o| o| .| .| .| .| o o'`, the function will split it into individual notes `['o', 'o|', '.', 'o|', 'o|', '.', '.', '.', '.', 'o', 'o']`. It will then iterate over each note, and based on the note, it will add the corresponding number of beats to the `beats` array. The final `beats` array will be `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.

If the function encounters an invalid note, it will throw an error with a message indicating the invalid note.

The function finally returns the `beats` array.