  var count = 0;
  for (const c of s) {
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
      count += 1;
    }
  }
  return count;
}



