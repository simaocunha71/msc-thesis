  const compare_by_point = (a, b) => {
    const a_sum = sumDigits(a);
    const b_sum = sumDigits(b);

    if (a_sum > b_sum) {
      return 1;
    } else if (a_sum < b_sum) {
      return -1;
    } else {
      return a - b;
    }
  };

  const sumDigits = (n) => {
    let sum = 0;
    while (n > 0) {
      sum += n % 10;
      n = Math.floor(n / 10);
    }
    return sum;
  };

  return nums.sort(compare_by_point);
}



