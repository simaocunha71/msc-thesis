  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i].toUpperCase()) {
      sum += s[i].charCodeAt();
    }
  }
  return sum;
}



