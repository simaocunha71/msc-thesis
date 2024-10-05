  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= 'A' && s[i] <= 'Z') {
      sum += s.charCodeAt(i);
    }
  }
  return sum;
}