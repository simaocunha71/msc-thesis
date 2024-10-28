Here is the solution using a simple state machine to parse the input string:
```javascript
const parseMusic = (music_string) => {
  const notes = [];
  let beatCount = 0;
  let noteType = '';

  for (let i = 0; i < music_string.length; i++) {
    const char = music_string[i];

    if (char === 'o') {
      noteType = 'whole';
      beatCount = 4;
    } else if (char === '|') {
      if (noteType === 'whole') {
        noteType = 'half';
        beatCount = 2;
      } else if (noteType === 'half') {
        noteType = 'quater';
        beatCount = 1;
      }
    } else if (char === '.') {
      if (noteType === 'quater') {
        notes.push(beatCount);
        beatCount = 0;
        noteType = '';
      }
    }

    if (i === music_string.length - 1 && noteType !== '') {
      notes.push(beatCount);
    }
  }

  return notes;
};
```
Here's a breakdown of the code:

1. We initialize an empty array `notes` to store the parsed notes, and two variables `beatCount` and `noteType` to keep track of the current note's duration and type.
2. We iterate through each character in the input string.
3. If the character is 'o', we set `noteType` to 'whole' and `beatCount` to 4.
4. If the character is '|', we update `noteType` and `beatCount` based on the current `noteType`. If `noteType` is 'whole', we set it to 'half' and `beatCount` to 2. If `noteType` is 'half', we set it to 'quater' and `beatCount` to 1.
5. If the character is '.', we push the current `beatCount` to the `notes` array and reset `beatCount` and `noteType` to 0 and '', respectively.
6. At the end of the iteration, if there's a remaining `beatCount` and `noteType`, we push the remaining `beatCount` to the `notes` array.
7. Finally, we return the `notes` array.