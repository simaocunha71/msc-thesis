  let result = 0;

  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (i % 2 == 0 && c.toUpperCase() == c) {
      result += 1;
    }
  }

  return result;
}



