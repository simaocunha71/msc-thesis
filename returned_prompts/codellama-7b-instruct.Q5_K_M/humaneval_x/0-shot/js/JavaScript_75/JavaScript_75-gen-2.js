const isMultiplyPrime = (a) => {
  let count = 0;
  for (let i = 2; i < a; i++) {
    if (a % i === 0) {
      count++;
    }
  }
  if (count === 2) {
    return true;
  } else {
    return false;
  }
}
