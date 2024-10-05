```
const parseMusic = (music_string) => {
  const beatsPerNote = {
    'o': 4,
    'o|': 2,
    '.|': 1,
  };
  const notes = music_string.split(' ');
  return notes.map(note => beatsPerNote[note]);
};
```


The `parseMusic` function takes a string of musical notes as input and returns a list of integers representing how many beats each note lasts. The function uses a dictionary `beatsPerNote` to map each note to its corresponding number of beats. It then splits the input string into individual notes using the `split` method, and uses the `map` method to convert each note to its corresponding number of beats.

In the example output, the input string `'o o| .| o| o| .| .| .| .| o o'` is split into the following notes: `['o', 'o|', '.', 'o|', 'o|', '.', '|', '.', '.', '.', 'o', 'o']`. The `map` method is then applied to this array, and the resulting array is `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`, which represents the number of beats each note lasts.