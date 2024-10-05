  if (strings.length == 0) {
    return null;
  } else {
    let max_string = strings[0];
    for (const s of strings) {
      if (s.length > max_string.length) {
        max_string = s;
      }
    }
    return max_string;
  }
}