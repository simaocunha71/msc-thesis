  let count = 0;
  for (let i = 11; i < n; i += 11) {
    count += i.toString().split('').reduce((acc, c) => acc + (c == '7'), 0);
  }
  for (let i = 13; i < n; i += 13) {
    count += i.toString().split('').reduce((acc, c) => acc + (c == '7'), 0);
  }
  return count;
}