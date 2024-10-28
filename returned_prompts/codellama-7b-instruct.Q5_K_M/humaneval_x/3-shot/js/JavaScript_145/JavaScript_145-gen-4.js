  const compare = (a, b) => {
    const a_sum = a.reduce((a, b) => a + b);
    const b_sum = b.reduce((a, b) => a + b);

    if (a_sum != b_sum) {
      return a_sum - b_sum;
    } else {
      return a.indexOf(a) - b.indexOf(b);
    }
  }

  return nums.sort(compare);
}



