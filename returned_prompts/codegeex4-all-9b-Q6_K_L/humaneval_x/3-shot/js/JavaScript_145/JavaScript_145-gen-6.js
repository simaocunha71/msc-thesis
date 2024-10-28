  const compare = (a, b) => {
    var a_sum = 0;
    var b_sum = 0;
    for (const digit of a.toString()) {
      a_sum += parseInt(digit);
    }
    for (const digit of b.toString()) {
      b_sum += parseInt(digit);
    }
    if (a_sum < b_sum) {
      return -1;
    } else if (a_sum > b_sum) {
      return 1;
    } else {
      return a - b;
    }
  };

  return nums.sort(compare);
}