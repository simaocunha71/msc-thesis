  let result = array.slice();
  result.sort((a, b) => {
    let sum = a + b;
    if (sum % 2 == 0) {
      return b - a;
    } else {
      return a - b;
    }
  });
  return result;
}