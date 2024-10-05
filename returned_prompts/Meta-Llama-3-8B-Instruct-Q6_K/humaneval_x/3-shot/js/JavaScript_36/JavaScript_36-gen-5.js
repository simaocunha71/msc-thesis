  let count = 0;
  for (let i = 11; i < n; i += 11) {
    if ((i % 13 === 0) || (i % 11 === 0)) {
      count += String(i).split('').filter(c => c === '7').length;
    }
  }
  for (let i = 13; i < n; i += 13) {
    if (i % 11 === 0) {
      count += String(i).split('').filter(c => c === '7').length;
    }
  }
  return count;
}
//  or
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 11; i < n; i++) {
    if ((i % 13 === 0) || (i % 11 === 0)) {
      count += String(i).split('').filter(c => c === '7').length;
    }
  }
  return count;
}
//  or
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 11; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      count += (String(i).split('').filter(c => c === '7').length);
    }
  }
  return count;
}