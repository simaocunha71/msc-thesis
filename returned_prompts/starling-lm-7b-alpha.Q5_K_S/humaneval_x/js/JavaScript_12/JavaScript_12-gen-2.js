  if (strings.length == 0) {
    return null;
  }

  let longest = strings[0];
  for (const str of strings) {
    if (str.length > longest.length) {
      longest = str;
    }
  }

  return longest;
}



