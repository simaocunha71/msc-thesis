  var sum = 0;
  for (const c of s) {
    if (c.toUpperCase() != c) {
      sum += c.toUpperCase().charCodeAt(0);
    }
  }
  return sum;
}



