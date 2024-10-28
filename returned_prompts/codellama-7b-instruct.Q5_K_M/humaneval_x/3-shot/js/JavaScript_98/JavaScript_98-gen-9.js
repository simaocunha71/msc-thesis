  var count = 0;
  for (var i = 0; i < s.length; i++) {
    if (i % 2 == 0 && 'AEIOU'.includes(s[i].toUpperCase())) {
      count += 1;
    }
  }
  return count;
}



