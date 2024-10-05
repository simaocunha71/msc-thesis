  let sum = 0;
  for (const char of s) {
    if (char.toUpperCase() != char) {
      sum += char.charCodeAt(0);
    }
  }
  return sum;
}