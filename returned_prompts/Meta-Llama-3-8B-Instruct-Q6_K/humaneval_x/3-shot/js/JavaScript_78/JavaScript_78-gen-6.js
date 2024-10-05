  let count = 0;
  for (let i = 0; i < num.length; i++) {
    if (['2', '3', '5', '7', 'B', 'D'].includes(num[i])) {
      count++;
    }
  }
  return count;
}