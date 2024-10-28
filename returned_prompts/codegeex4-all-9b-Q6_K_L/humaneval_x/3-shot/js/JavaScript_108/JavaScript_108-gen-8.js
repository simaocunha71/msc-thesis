  let count = 0;
  for (const num of arr) {
    let sum = 0;
    let num_str = Math.abs(num).toString();
    for (const c of num_str) {
      sum += parseInt(c);
    }
    if (sum > 0) {
      count += 1;
    }
  }
  return count;
}



