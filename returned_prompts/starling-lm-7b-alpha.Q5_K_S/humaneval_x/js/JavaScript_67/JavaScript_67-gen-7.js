  let arr = s.split(' ');
  let count = 0;
  for (const a of arr) {
    if (a == 'apples') {
      count += 1;
    } else if (a == 'oranges') {
      count += 2;
    }
  }
  return n - count;
}



