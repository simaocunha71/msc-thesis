  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (c.toUpperCase() === c) {
      sum += c.charCodeAt(0);
    }
  }
  return sum;
}