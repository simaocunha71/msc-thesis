  let musicNotes = music_string.split(" ");
  let beatsPerNote = [];

  musicNotes.forEach(note => {
    switch(note) {
      case 'o':
        beatsPerNote.push(4);
        break;
      case 'o|':
        beatsPerNote.push(2);
        break;
      case '.|':
        beatsPerNote.push(1);
        break;
      default:
        break;
    }
  });

  return beatsPerNote;
};

console.log(parseMusic('o o| .| o| o| .| .| .| .| o o')); // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

</div>


<div id='2'>

## 2. Create a function to calculate the sum of all even numbers in a list

