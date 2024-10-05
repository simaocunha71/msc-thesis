  return nums.sort((a, b) => {
    let a_sum = a.toString().split('').reduce((acc, num) => acc + parseInt(num), 0);
    let b_sum = b.toString().split('').reduce((acc, num) => acc + parseInt(num), 0);
    if (a_sum < b_sum) {
      return -1;
    } else if (a_sum > b_sum) {
      return 1;
    } else {
      return nums.indexOf(a) - nums.indexOf(b);
    }
  });
}