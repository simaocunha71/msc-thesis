  let sum = 0;
  for (let c of s) {
    if (c == c.toUpperCase()) {
      sum += c.charCodeAt(0);
    }
  }
  return sum;
}



