  let count = 0;
  for (let num of arr) {
    if (Math.abs(num) > 0) {
      let sum = 0;
      let num_str = Math.abs(num) + '';
      for (let i = 0; i < num_str.length; i++) {
        sum += parseInt(num_str[i]);
      }
      if (sum > 0) {
        count++;
      }
    }
  }
  return count;
}