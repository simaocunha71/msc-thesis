  // Initialize an empty list to store the beats for each note
  let beats_per_note = [];

  // Split the string into individual notes
  let notes = music_string.split(' ');

  // Iterate over each note
  for (let note of notes) {
    // Initialize a counter for the beats in the current note
    let beats = 0;

    // If the note is a half or quater note, count two beats
    if (note === 'o|' || note === '.|') {
      beats = 2;
    }
    // Otherwise, a whole note lasts for four beats
    else {
      beats = 4;
    }

    // Add the number of beats for the current note to the list
    beats_per_note.push(beats);
  }

  // Return the list of beats
  return beats_per_note;
};

console.log(parseMusic('o o| •| o| o| •| •| •| •| o o'));
// Expected output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

### Solution 2:

```javascript
const parseMusic = (musicString) => {
  let beatCounts = [];
  let noteTypes = {
    'o': 4,
    'o|': 2,
    '.|': 1
  };

  musicString.split(' ').forEach(note => {
    beatCounts.push(noteTypes[note]);
  });

  return beatCounts;
};

console.log(parseMusic('o o| .| o| o| .| .| .| .| o o'));
// Expected output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

### Solution 3:

```javascript
const parseMusic = (str) => {
    let notes = {
        'o': 4,
       