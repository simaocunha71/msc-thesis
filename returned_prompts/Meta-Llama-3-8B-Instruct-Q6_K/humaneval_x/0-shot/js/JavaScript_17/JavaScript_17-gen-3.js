Here is the solution:
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

1. We split the input string into an array of individual notes using the `split` method.
2. We initialize an empty array `beats` to store the number of beats for each note.
3. We iterate through each note in the array and use a `switch` statement to determine the number of beats it lasts. We use the same legend as described in the problem statement.
4. We push the corresponding number of beats onto the `beats` array.
5. Finally, we return the `beats` array.

You can test the function with the example input provided in the problem statement:
```javascript
console.log(parseMusic('o o| .| o| o| .| .| .| .| o o')); // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```