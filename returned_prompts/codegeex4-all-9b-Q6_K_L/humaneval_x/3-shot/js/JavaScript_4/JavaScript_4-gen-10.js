  let mean = 0;
  for (const num of numbers) {
    mean += num;
  }
  mean /= numbers.length;

  let total = 0;
  for (const num of numbers) {
    total += Math.abs(num - mean);
  }
  total /= numbers.length;

  return total;
}



