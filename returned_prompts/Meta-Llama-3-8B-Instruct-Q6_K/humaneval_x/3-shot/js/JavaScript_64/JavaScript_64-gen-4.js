  let count = 0;
  for (const char of s.toLowerCase()) {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u' || char === 'y') {
      if (char === 'y' && s[s.length - 1] === 'y') {
        continue;
      }
      count++;
    }
  }
  return count;
}