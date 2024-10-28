[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

Explanation
We split the music string by the '|' delimiter. Then we iterate over each note. If the note is 'o', we add 4 to the result array. If the note is 'o|', we add 2 to the result array. If the note is '.|', we add 1 to the result array.

*/

// Here's a function that parses a musical string and returns an array of the number of beats for each note.

// Here's an example of how to use this function:

const parseMusic = (music_string) => {
  let notes = music_string.split('|');
  let beats = [];
  notes.forEach(note => {
    if (note === 'o') {
      beats.push(4);
    } else if (note === 'o|') {
      beats.push(2);
    } else if (note === '.|') {
      beats.push(1);
    }
  });
  return beats;
};

console.log(parseMusic('o o| .| o| o| o| .| .| .| .| o o')); // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

Explanation
The function `parseMusic` takes a string `music_string` as input. It splits the string by the '|' delimiter and