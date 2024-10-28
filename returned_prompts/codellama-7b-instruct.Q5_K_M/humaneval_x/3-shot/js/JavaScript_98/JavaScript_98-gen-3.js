  var count = 0;
  for (var i = 0; i < s.length; i += 2) {
    if (s[i] === s[i].toUpperCase()) {
      count += 1;
    }
  }
  return count;
}



