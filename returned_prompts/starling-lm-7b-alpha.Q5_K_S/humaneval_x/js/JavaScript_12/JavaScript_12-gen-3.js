  if (strings.length == 0) {
    return null;
  }

  let longestString = strings[0];
  for (const s of strings) {
    if (s.length > longestString.length) {
      longestString = s;
    }
  }

  return longestString;
}



