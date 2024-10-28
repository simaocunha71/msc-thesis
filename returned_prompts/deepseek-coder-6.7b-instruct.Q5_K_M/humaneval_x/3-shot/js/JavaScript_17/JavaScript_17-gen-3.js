  var notes = music_string.split(' ');
  var result = [];

  for  (var i = 0; i < notes.length; i++) {
    switch (notes[i]) {
      case 'o':
        result.push(4);
        break;
      case 'o|':
        result.push(2);
        break;
      case '.|':
        result.push(1);
        break;
    }
  }

  return result;
}



