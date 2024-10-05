  var seen_chars 
  seen_chars = new Set();

  for  (const char of string.toLowerCase()) {
    seen_chars.add(char);
  }

  return seen_chars.size;
}



