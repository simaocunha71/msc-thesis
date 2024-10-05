  let count = 0;
  for (let i = 11; i < n; i++) {
    if ((i % 11 === 0) || (i % 13 === 0)) {
      count += (i.toString()).split('').reduce((acc, cur) => acc + (cur === '7'), 0);
    }
  }
  for (let i = 13; i < n; i++) {
    if (i % 13 === 0) {
      count += (i.toString()).split('').reduce((acc, cur) => acc + (cur === '7'), 0);
    }
  }
  return count;
}  // This function is a bit complex and may not work correctly for very large inputs due to the limitations of JavaScript's integer type. For such inputs, you might need to use a library that supports arbitrary-precision arithmetic.