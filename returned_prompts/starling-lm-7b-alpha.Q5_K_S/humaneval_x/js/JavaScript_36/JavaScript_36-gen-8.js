  let result = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      let str = i.toString();
      if (str.includes('7')) {
        result += 1;
      }
    }
  }
  return result;
}



