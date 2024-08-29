  if (strings.length === 0) {
    return null;
  } else {
    let longest = strings[0];
    for (let i = 1; i < strings.length; i++) {
      if (longest.length < strings[i].length) {
        longest = strings[i];
      }
    }
    return longest;
  }
}



