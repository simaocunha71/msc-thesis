  let beat_counts = [];
  let music_notes = music_string.split(' ');

  for (let i = 0; i < music_notes.length; i++) {
    switch (music_notes[i]) {
      case 'o':
        beat_counts.push(4);
        break;
      case 'o|':
        beat_counts.push(2);
        break;
      case '.|':
        beat_counts.push(1);
        break;
    }
  }

  return beat_counts;
};

console.log(parseMusic('o o| .| o| o| .| .| .| .| o o'));

```

This program works by first splitting the input string into an array of individual notes. It then loops over this array, and for each note, it adds the appropriate number of beats to the `beat_counts` list. Finally, it returns this list.

The time complexity is O(n), where n is the number of notes in the input string, because it needs to loop over all the notes. The space complexity is also O(n), because it creates a new list to store the beat counts.

This program assumes that the input string will always be in the correct format. If this is not the case, you would need to add error checking to handle invalid inputs.
"""

tests = [
    ("o o| .| o| o| .| .| .| .| o o", [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]),
    ("o o| .| o| o| o| .| .| .| o o", [4, 2, 1, 2, 4, 2, 1, 1, 1, 4, 4]),
    ("o| o| o| o| o| o| o| o| o| o|", [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
    (".", [1]),
    ("", []),
]

for