  var result = 0;
  var seen = {};

  for (const c of string) {
    if (!seen[c]) {
      seen[c] = true;
      result += 1;
    }
  }

  return result;
}



