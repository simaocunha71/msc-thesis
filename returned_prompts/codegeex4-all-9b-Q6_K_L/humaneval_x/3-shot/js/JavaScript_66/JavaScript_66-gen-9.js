  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (c >= 'A' && c <= 'Z') {
      sum += c.charCodeAt(0);
    }
  }
  return sum;
}



