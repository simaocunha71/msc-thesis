  let count = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      let str = i.toString();
      for (let j = 0; j < str.length; j++) {
        if (str.charAt(j) == '7') {
          count += 1;
        }
      }
    }
  }
  return count;
}