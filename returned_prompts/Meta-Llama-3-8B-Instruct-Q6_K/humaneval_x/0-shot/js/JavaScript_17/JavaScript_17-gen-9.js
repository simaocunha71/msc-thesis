Here is the solution:
```
const parseMusic = (music_string) => {
  const notes = music_string.split(' ');
  const beats = [];

  for (let note of notes) {
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
Here's an explanation of the solution:

1. We split the input string into an array of individual notes using the `split` method with a space character as the separator.
2. We initialize an empty array `beats` to store the number of beats for each note.
3. We iterate over each note in the array using a `for...of` loop.
4. We use a `switch` statement to determine the number of beats for each note based on the legend provided. For each valid note, we push the corresponding number of beats onto the `beats` array.
5. If a note is invalid (i.e., not one of the three recognized notes), we throw an error.
6. Finally, we return the `beats` array, which contains the number of beats for each note in the input string.

You can test the function with the example input provided to see that it returns the expected output:
```
console.log(parseMusic('o o| .| o| o| .| .| .| .| o o'));
// Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` Q.E.D.! 🎶👏

Please note that this solution assumes that the input string is well-formed and does not contain any invalid notes. If you want to handle invalid notes more robustly, you may want to consider using a regular expression or a more advanced parsing technique. 😊 