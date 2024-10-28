  // Split the string into an array of notes
  let notes = music_string.split(" ");

  // Initialize an empty array to store the length of each note
  let noteLengths = [];

  // Loop through each note
  for (let i = 0; i < notes.length; i++) {

    // Initialize a variable to store the length of the current note
    let noteLength = 0;

    // Split the current note into an array of symbols
    let symbols = notes[i].split("");

    // Loop through each symbol in the current note
    for (let j = 0; j < symbols.length; j++) {

      // Increment the length of the current note based on the symbol
      if (symbols[j] === 'o') {
        noteLength += 4;
      } else if (symbols[j] === '|') {
        noteLength /= 2;
      }
    }

    // Add the length of the current note to the list of note lengths
    noteLengths.push(noteLength);
  }

  // Return the list of note lengths
  return noteLengths;
}

console.log(parseMusic('o o| 。| o| o| 。| 。| 。| 。| o o')); // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

/* Explanation of the function:

The function `parseMusic` takes a string `music_string` as input.
It first splits the string into an array `notes` of individual notes.
Then, it initializes an empty array `noteLengths` to store the length of each note.

For each note in `notes`, it first initializes `noteLength` to 0.
Then, it splits the note into an array `symbols` of individual symbols.

For each symbol in `symbols`, it increments `noteLength` based on the symbol.
If the symbol is 'o', it adds 4 to `noteLength`.
If the symbol is '|', it divides `noteLength` by 2.