  const sums = nums.map(num => {
    return { num: num, points: num.toString().split('').reduce((acc, val) => acc + +val, 0) };
  });

  return sums.sort((a, b) => a.points - b.points || a.num - b.num);
}



