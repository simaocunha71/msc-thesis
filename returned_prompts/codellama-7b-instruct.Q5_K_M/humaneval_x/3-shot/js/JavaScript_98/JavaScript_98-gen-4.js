  var count = 0;
  var even_index = 0;

  for (var i = 0; i < s.length; i++) {
    if (even_index % 2 == 0) {
      if (s[i].toUpperCase() == 'A' || s[i].toUpperCase() == 'E' || s[i].toUpperCase() == 'O' || s[i].toUpperCase() == 'I' || s[i].toUpperCase() == 'U') {
        count++;
      }
    }
    even_index++;
  }

  return count;
}



