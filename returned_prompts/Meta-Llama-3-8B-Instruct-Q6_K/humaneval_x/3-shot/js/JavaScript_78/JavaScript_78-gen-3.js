  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let digit = parseInt(num[i], 16);
    if (digit >= 2 && digit <= 7) {
      count++;
    }
  }
  return count;
}