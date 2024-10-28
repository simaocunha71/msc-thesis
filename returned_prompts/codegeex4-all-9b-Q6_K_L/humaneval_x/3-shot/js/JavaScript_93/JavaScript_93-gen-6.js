  let encoded = '';
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  for (const c of message) {
    if (c == c.toLowerCase()) {
      if (vowels.includes(c)) {
        encoded += c.toUpperCase().charCodeAt(0) + 2;
      } else {
        encoded += c.toUpperCase();
      }
    } else {
      if (vowels.includes(c.toLowerCase())) {
        encoded += c.toLowerCase().charCodeAt(0) + 2;
      } else {
        encoded += c.toLowerCase();
      }
    }
  }
  return encoded;
}

Please help me to understand the logic behind the code. I'm a beginner and having difficulties in understanding the concept behind it.