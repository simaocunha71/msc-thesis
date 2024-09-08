  let result = "";
  const vowels = ["a", "e", "i", "o", "u"];

  for (const c of message) {
    if (c == c.toLowerCase()) {
      result += c.toUpperCase();
    } else if (c == c.toUpperCase()) {
      result += c.toLowerCase();
    } else if (vowels.includes(c)) {
      const index = vowels.indexOf(c);
      result += vowels[(index + 2) % vowels.length];
    } else {
      result += c;
    }
  }

  return result;
}



