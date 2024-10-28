  const upper = string.toUpperCase();
  var counter = 0;

  for (const c of upper) {
    if (c >= 'A' && c <= 'Z') {
      counter++;
    }
  }

  return counter;
}



