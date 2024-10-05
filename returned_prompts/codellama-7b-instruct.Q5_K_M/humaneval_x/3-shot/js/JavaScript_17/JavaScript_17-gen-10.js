  var result = [];

  for (let c of music_string) {
    switch (c) {
      case 'o':
        result.push(4);
        break;
      case '|':
        result.push(2);
        break;
      case '.':
        result.push(1);
        break;
    }
  }

  return result;
}



