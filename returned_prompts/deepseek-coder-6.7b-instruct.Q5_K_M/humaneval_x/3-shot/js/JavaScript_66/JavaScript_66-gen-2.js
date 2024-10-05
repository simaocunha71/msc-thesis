  let sum = 0;
  for(let i = 0; i < s.length; i++) {
    let code = s.charCodeAt(i);
    if(code >= 65 && code <= 90) {
      sum += code;
    }
  }
  return sum;
}



