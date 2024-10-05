  var result = 0;
  for (const num of arr) {
    if (num > 0 || (num < 0 && num.toString().split('').reduce((a, b) => a + b) > 0)) {
      result += 1;
    }
  }
  return result;
}



