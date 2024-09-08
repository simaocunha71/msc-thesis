  function count_digit_sum(n) {
    let result = 0;
    while (n > 0) {
      result += n % 10;
      n = Math.floor(n / 10);
    }
    return result;
  }

  let count = 0;
  for (const n of arr) {
    if (count_digit_sum(n) > 0) {
      count += 1;
    }
  }
  return count;
}



