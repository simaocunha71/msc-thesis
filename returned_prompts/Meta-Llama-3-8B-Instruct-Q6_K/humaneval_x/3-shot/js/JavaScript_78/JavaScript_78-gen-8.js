  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let digit = parseInt(num[i], 16);
    if ([2, 3, 5, 7, 11, 13].includes(digit)) {
      count++;
    }
  }
  return count;
}