  let count = 0;
  for (const num of nums) {
    if (num > 10 && (num % 10 >= 7) && (num % 10 <= 9) && (Math.floor(num / 10) % 2 != 0)) {
      count++;
    }
  }
  return count;
}



