  const sums = nums.map((num, i) => ({num, i, sum: num.toString().split('').reduce((acc, cur) => acc + +cur, 0)}));
  sums.sort((a, b) => {
    if (a.sum == b.sum) {
      return a.i - b.i;
    }
    return a.sum - b.sum;
  });
  return sums.map(n => n.num);
}



