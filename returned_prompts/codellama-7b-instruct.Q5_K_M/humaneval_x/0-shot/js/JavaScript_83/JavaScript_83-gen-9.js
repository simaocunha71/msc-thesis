  const nums = [];
  for (let i = 1; i <= n; i++) {
    nums.push(i);
  }
  return nums.filter(num => num.toString().startsWith("1") || num.toString().endsWith("1")).length;
};
