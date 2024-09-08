  let sum = 0;
  for (const c of s) {
    if (c >= 'A' && c <= 'Z') {
      sum += c.charCodeAt(0);
    }
  }
  return sum;
}



