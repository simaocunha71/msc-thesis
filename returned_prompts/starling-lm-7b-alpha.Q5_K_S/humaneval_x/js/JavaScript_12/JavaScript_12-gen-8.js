  if (strings.length == 0) {
    return null;
  }

  var longest = strings[0];
  for (const s of strings) {
    if (s.length > longest.length) {
      longest = s;
    }
  }

  return longest;
}



