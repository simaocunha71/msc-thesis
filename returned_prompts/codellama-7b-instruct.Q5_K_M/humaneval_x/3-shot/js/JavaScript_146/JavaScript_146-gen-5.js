  let count = 0;

  for (let num of nums) {
    if (num > 10 && (num % 10) % 2 === 1) {
      count += 1;
    }
  }

  return count;
}



