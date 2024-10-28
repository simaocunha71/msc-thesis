  var count = 0;
  for (var i = 0; i < S.length; i++) {
    if (S[i] == '.') {
      i++;
    }
    if (S[i] == '?' || S[i] == '!') {
      i++;
    }
    if (S[i] == 'I') {
      count++;
    }
  }
  return count;
}



