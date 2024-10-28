  var notes = music_string.split(' ');
  var beats = [];

  for (const note of notes) {
    switch (note) {
      case 'o':
        beats.push(4);
        break;
      case 'o|':
        beats.push(2);
        break;
      case '.|':
        beats.push(1);
        break;
    }
  }

  return beats;
}



