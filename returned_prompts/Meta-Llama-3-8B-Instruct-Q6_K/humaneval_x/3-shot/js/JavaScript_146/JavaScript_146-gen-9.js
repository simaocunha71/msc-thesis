  let count = 0;
  for (let num of nums) {
    if (num > 10 && parseInt(String(num)[0]) % 2 !== 0 && parseInt(String(num)[String(num).length - 1]) % 2 !== 0) {
      count++;
    }
  }
  return count;
} 



