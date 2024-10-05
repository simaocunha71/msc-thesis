Here's how you might parse the music string:

```javascript
const parseMusic = (music_string) => {
  const music_notes = music_string.split(' ');
  const beats = [];
  
  music_notes.forEach(note => {
    if (note === 'o') {
      beats.push(4);
    } else if (note === 'o|') {
      beats.push(2);
    } else if (note === '.|') {
      beats.push(1);
    }
  });
  
  return beats;
}
```

This function splits the music string into an array of individual notes, then iterates over each note and adds the corresponding number of beats to the `beats` array.

We use the `if-else` statement to check which type of note is present and then push the corresponding number of beats to the `beats` array.