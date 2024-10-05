  var count = 0;

  for (let i = 0; i < string.length; i++) {
    if (string.startsWith(substring, i)) {
      count += 1;
      i += substring.length - 1;
    }
  }

  return count;
}



