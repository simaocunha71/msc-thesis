  let count = 0;
  for (let i = 11; i < n; i += 11) {
    if (String(i).includes('7')) {
      count++;
    }
  }
  for (let i = 13; i < n; i += 13) {
    if (String(i).includes('7')) {
      count++;
    }
  }
  return count;
}  // or you can use a single loop with modulo operation
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 11; i < n; i++) {
    if ((i % 11 == 0 || i % 13 == 0) && String(i).includes('7')) {
      count++;
    }
  }
  return count;
}