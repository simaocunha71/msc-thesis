  var count = 0;

  for (let i = 0; i < string.length; i++) {
    if (string.indexOf(substring, i) == i) {
      count++;
      i += substring.length - 1;
    }
  }

  return count;
}



