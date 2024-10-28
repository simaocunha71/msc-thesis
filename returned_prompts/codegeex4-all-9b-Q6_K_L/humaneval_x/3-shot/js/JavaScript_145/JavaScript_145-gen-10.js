  return nums.sort((a, b) => {
    var sum_a = a.toString().split('').reduce((acc, num) => acc + parseInt(num), 0);
    var sum_b = b.toString().split('').reduce((acc, num) => acc + parseInt(num), 0);
    if (sum_a == sum_b) {
      return nums.indexOf(a) - nums.indexOf(b);
    } else {
      return sum_a - sum_b;
    }
  });
}



