  let result = [0, 0];
  let s = Math.abs(num).toString();
  for (let i = 0; i < s.length; i++) {
    if (s[i] % 2 == 0) {
      result[0] += 1;
    } else {
      result[1] += 1;
    }
  }
  return result;
}



