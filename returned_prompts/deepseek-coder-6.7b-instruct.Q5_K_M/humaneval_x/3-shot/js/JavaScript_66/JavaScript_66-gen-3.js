  let sum = 0;
  for(let i = 0; i < s.length; i++) {
    if(s[i] === s[i].toUpperCase() && isNaN(Number(s[i]))) {
      sum += s[i].charCodeAt(0);
    }
  }
  return sum;
}



