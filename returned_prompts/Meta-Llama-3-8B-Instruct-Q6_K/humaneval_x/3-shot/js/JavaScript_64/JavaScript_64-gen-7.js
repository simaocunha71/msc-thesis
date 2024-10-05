  let count = 0;
  for (let char of s.toLowerCase()) {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
      count++;
    } else if (char === 'y' && s.endsWith(char)) {
      count++;
    }
  }
  return count;
}
