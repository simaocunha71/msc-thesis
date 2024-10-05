  var count = 0;
  for (let i = 0; i < string.length; i++) {
    if (string.slice(i, i + substring.length) == substring) {
      count += 1;
    }
  }
  return count;
}



