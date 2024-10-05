  let sum = 0;
  for (let char of s) {
    if (char.toUpperCase() != char) {
      sum += char.charCodeAt(0);
    }
  }
  return sum;
}