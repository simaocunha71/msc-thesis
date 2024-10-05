```javascript
const parseMusic = (music_string) => {
  const notes = music_string.split(' ');
  const beats = [];
  for (const note of notes) {
    switch (note) {
      case 'o': beats.push(4); break;
      case 'o|': beats.push(2); break;
      case '.|': beats.push(1); break;
      default: throw new Error(`Unknown note: ${note}`);
    }
  }
  return beats;
};
```



Explanation:
The function `parseMusic` takes a string `music_string` as input, which represents musical notes in a special ASCII format.

First, we split the input string into an array of individual notes using the `split` method with a space character as the separator.

Then, we iterate over the array of notes using a `for...of` loop. For each note, we use a `switch` statement to determine the number of beats it lasts.

- If the note is 'o', it lasts 4 beats, so we push 4 to the `beats` array.
- If the note is 'o|', it lasts 2 beats, so we push 2 to the `beats` array.
- If the note is '.|', it lasts 1 beat, so we push 1 to the `beats` array.
- If the note is anything else, we throw an error, because it's not a recognized note.

Finally, we return the `beats` array, which contains the number of beats for each note in the input string.