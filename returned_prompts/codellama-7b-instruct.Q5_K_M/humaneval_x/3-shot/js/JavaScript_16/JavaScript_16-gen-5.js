  var char_counts = {};
  for (const c of string) {
    if (char_counts[c] == undefined) {
      char_counts[c] = 1;
    } else {
      char_counts[c] += 1;
    }
  }
  return Object.keys(char_counts).length;
}



