  let max_length = -Infinity;
  let longest_string = null;

  for (const s of strings) {
    if (s.length > max_length) {
      max_length = s.length;
      longest_string = s;
    }
  }

  return longest_string;
}



