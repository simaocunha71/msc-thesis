  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i].toUpperCase() !== s[i]) {
      sum += s[i].charCodeAt(0);
    }
  }
  return sum;
}



