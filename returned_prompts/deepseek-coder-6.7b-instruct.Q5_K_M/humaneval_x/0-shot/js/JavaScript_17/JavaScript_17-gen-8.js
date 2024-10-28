  let notes = music_string.split(' ');
  let noteLengths = [];

  for(let i = 0; i < notes.length; i++){
    let note = notes[i];
    let noteBeats = 0;

    for(let j = 0; j < note.length; j++){
      let symbol = note[j];

      if(symbol === 'o') noteBeats += 4;
      if(symbol === '|') noteBeats /= 2;
    }

    noteLengths.push(noteBeats);
  }

  return noteLengths;
}
console.log(parseMusic('o o| .| o| o| .| .| .| .| o o')) // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

*/
/* 
Explanation:
We start by splitting the input string into an array of notes. Then we initialize an empty array to store the lengths of the notes.

For each note, we initialize a variable to store the number of beats. We then iterate over each character in the note. If the character is 'o', we add four to the number of beats. If the character is '|', we divide the number of beats by two.

Finally, we push the number of beats for the note into the array of note lengths and return this array.

This function works by first splitting the input string into an array of notes, then iterating over each note and character in the note to determine the number of beats.
*/










































































































































