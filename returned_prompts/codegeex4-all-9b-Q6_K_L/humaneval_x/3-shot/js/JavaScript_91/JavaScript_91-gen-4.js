  var count = 0;
  for (var i = 0; i < S.length; i++) {
    if (S[i] == 'I') {
      if (S[i + 1] == ' ') {
        count += 1;
      }
    }
  }
  return count;
}



