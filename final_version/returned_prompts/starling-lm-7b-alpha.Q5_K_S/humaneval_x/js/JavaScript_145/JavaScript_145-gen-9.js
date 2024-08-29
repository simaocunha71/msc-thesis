  const sums = nums.map((x) => {
    return { num: x, digitSum: (+x + '').split('').reduce((a, b) => a + +b, 0) };
  });

  const sortedSums = sums.sort((a, b) => {
    if (a.digitSum < b.digitSum) {
      return -1;
    } else if (a.digitSum > b.digitSum) {
      return 1;
    } else {
      return a.num - b.num;
    }
  });

  const sortedNums = sortedSums.map((x) => x.num);

  return sortedNums;
}



