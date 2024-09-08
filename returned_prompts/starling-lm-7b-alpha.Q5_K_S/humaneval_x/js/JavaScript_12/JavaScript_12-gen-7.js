  if (strings.length == 0) {
    return null;
  } else {
    let max_length = 0;
    let max_string = null;
    for (const s of strings) {
      if (s.length > max_length) {
        max_length = s.length;
        max_string = s;
      }
    }
    return max_string;
  }
}



