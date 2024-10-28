  let count = 0;

  for (let num of nums) {
    if (num > 10 && ((num % 10 > 1 && num % 10 < 9) || (num % 100 > 10 && num % 100 < 90))) {
      count++;
    }
  }

  return count;
}



