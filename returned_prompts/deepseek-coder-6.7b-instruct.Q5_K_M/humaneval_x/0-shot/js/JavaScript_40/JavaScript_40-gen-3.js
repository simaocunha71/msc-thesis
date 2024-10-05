  l.sort((a, b) => a - b);
  for (let i = 0; i < l.length - 2; i++) {
    if (i > 0 && l[i] === l[i - 1]) {
      continue;
    }
    let j = i + 1;
    let k = l.length - 1;
    while (j < k) {
      const sum = l[i] + l[j] + l[k];
      if (sum < 0) {
        j++;
      } else if (sum > 0) {
        k--;
      } else {
        return true;
      }
    }
  }
  return false;
};

module.exports = triplesSumToZero;

*/


/*

