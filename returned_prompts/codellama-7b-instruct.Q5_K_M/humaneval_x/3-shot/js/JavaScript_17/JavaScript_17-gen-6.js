  var beats = [];

  for (let c of music_string) {
    if (c == 'o') {
      beats.push(4);
    } else if (c == '|') {
      beats.push(2);
    } else if (c == '.') {
      beats.push(1);
    }
  }

  return beats;
}



