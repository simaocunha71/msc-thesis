Here is the solution:

```javascript
const parseMusic = (music_string) => {
  const notes = music_string.split(' ');
  return notes.map(note => {
    if(note === 'o') {
      return 4;
    } else if(note === 'o|') {
      return 2;
    } else if(note === '.|') {
      return 1;
    } else {
      throw new Error('Invalid note: ' + note);
    }
  });
};
```

This solution splits the input string into an array of notes, then maps over the array and returns the corresponding number of beats for each note. If an invalid note is encountered, an error is thrown.