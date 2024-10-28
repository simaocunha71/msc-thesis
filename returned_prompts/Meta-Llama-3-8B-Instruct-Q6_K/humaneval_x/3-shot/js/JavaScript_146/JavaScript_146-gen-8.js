  let count = 0;
  for (let num of nums) {
    if (Math.abs(num) > 10) {
      let str = String(Math.abs(num));
      if (parseInt(str[0]) % 2 !== 0 && parseInt(str[str.length - 1]) % 2 !== 0) {
        count++;
      }
    }
  }
  return count;
}