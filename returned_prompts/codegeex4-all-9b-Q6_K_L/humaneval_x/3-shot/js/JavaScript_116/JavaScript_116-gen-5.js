  return arr.sort((a, b) => {
    if (countOnes(a) == countOnes(b)) {
      return a - b;
    } else {
      return countOnes(a) - countOnes(b);
    }
  });

  function countOnes(num) {
    return num.toString(2).split('').filter(c => c == '1').length;
  }
}