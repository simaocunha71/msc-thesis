  const lowercase_string = string.toLowerCase();
  const distinct_chars = new Set();

  for (const char of lowercase_string) {
    distinct_chars.add(char);
  }

  return distinct_chars.size;
}



