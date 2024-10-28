  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i].toUpperCase() === s[i]) {
      sum += s.charCodeAt(i);
    }
  }
  return sum;
}