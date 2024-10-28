```js
const parseMusic = (music_string) => {
  const notes = music_string.split(' ');
  return notes.map(note => {
    if (note === 'o') {
      return 4;
    } else if (note === 'o|') {
      return 2;
    } else if (note === '.|') {
      return 1;
    } else {
      return 0;
    }
  });
}
```
