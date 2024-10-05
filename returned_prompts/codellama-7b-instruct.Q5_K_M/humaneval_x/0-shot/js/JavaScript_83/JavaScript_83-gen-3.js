  const nums = [];
  for (let i = 1; i <= 9; i++) {
    nums.push(i);
  }
  for (let i = 10; i <= 99; i++) {
    nums.push(i);
  }
  return nums.filter(num => num.toString().startsWith("1") || num.toString().endsWith("1")).length;
}


