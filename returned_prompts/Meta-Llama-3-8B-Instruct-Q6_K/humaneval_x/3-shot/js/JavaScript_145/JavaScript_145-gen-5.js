  return nums.sort((a, b) => {
    let a_sum = a.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    let b_sum = b.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    if (a_sum === b_sum) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return a_sum - b_sum;
  });
}