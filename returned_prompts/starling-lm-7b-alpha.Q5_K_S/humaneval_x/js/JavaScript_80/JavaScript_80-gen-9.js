  if (s.length < 3) {
    return false;
  }
  var letters = {};
  for (const c of s) {
    if (letters[c] == undefined) {
      letters[c] = 1;
    } else {
      letters[c] += 1;
    }
    if (letters[c] > 1) {
      return false;
    }
  }
  return true;
}



