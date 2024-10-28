  // Initialize an empty array to store the beats
  let beats = [];
  // Split the string into an array of notes
  let notes = music_string.split(' ');

  // Iterate over the notes
  for(let i = 0; i < notes.length; i++){
    // For each note, split it into characters
    let note = notes[i].split('');
    // Initialize a counter for the beats
    let beatCount = 0;
    // Iterate over the characters
    for(let j = 0; j < note.length; j++){
      // If the character is 'o', add 4 to the beatCount
      if(note[j] === 'o'){
        beatCount += 4;
      }
      // If the character is '|', divide the beatCount by 2 (rounding down)
      else if(note[j] === '|'){
        beatCount = Math.floor(beatCount / 2);
      }
    }
    // Add the beatCount to the beats array
    beats.push(beatCount);
  }
  // Return the beats array
  return beats;
}

console.log(parseMusic('o o| ••| ••| ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••