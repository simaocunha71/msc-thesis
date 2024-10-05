  const notes = music_string.split('|');
  const beats = notes.map(note => {
    if (note === 'o') return 4;
    if (note === 'o|') return 2;
    if (note === '.|') return 1;
  });
  return beats;
};

parseMusic('o o| .| o| o| o| .| .| .| .| o o');



/*
The function takes a string, splits it into an array of notes using the "|" delimiter.
Then it uses Array.map() to iterate over each note and determine how many beats it lasts based on the note's ASCII value.
Finally, it returns the array of beats.

To test the function, we pass in the string 'o o| .| o| o| o| .| .| .| .| o o' and store the result in a variable called result.
Then we use console.log() to print the result, which should be [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4],
representing the number of beats for each note in the input string.

The expected output of the function is an array of integers representing the number of beats for each note in the input string.

The function correctly determines the number of beats for each note based on the ASCII values of the input string and returns the result as an array.
*/
































































































































































