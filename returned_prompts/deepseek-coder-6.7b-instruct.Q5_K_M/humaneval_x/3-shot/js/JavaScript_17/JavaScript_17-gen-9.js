  var notes = music_string.split(' ');
  var beat_counts = [];

  for  (const note of notes)  {
    switch(note)  {
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
}



