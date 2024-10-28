  let count = 0;

  for (let num of nums) {
    if (num > 10 && (Math.abs(num) % 10) % 2 == 1) {
      count++;
    }
  }

  return count;
}



