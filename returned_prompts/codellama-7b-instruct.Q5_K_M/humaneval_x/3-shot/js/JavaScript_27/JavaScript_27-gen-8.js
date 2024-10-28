  return string.toLowerCase().split('').map(function(char) {
    if (char.match(/[a-z]/)) {
      return char.toUpperCase();
    } else {
      return char.toLowerCase();
    }
  }).join('');
}



