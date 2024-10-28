```javascript
const parseMusic = (music_string) => {
  const notes = music_string.split(' ');
  return notes.map(note => {
    if (note === 'o') return 4;
    if (note === 'o|') return 2;
    if (note === '.|') return 1;
    throw new Error(`Invalid note: ${note}`);
  });
};
```  