Here is a possible solution:
```javascript
const parseMusic = (music_string) => {
  const notes = music_string.split(' ');
  const beats = [];
  for (const note of notes) {
    switch (note) {
      case 'o':
        beats.push(4);
        break;
      case 'o|':
        beats.push(2);
        break;
      case '.|':
        beats.push(1);
        break;
      default:
        throw new Error(`Invalid note: ${note}`);
    }
  }
  return beats;
};
```
Here's an explanation of the code:

1. We split the input string into individual notes using the `split` method with a space character as the separator.
2. We initialize an empty array `beats` to store the number of beats for each note.
3. We loop through each note in the array using a `for...of` loop.
4. We use a `switch` statement to determine the number of beats for each note based on the legend provided.
5. If the note is invalid, we throw an error.
6. Finally, we return the `beats` array.

You can test this function with the example input provided to see that it produces the correct output.