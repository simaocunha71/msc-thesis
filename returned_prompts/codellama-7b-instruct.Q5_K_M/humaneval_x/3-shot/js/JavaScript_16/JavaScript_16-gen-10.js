  var distinct_chars = [];
  for (const c of string.toLowerCase()) {
    if (!distinct_chars.includes(c)) {
      distinct_chars.push(c);
    }
  }
  return distinct_chars.length;
}



