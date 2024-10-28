  if (l.length < 3) {
    return false;
  }

  l.sort((a, b) => a - b);

  for (let i = 0; i < l.length - 2; i++) {
    if (i > 0 && l[i] === l[i - 1]) {
      continue;
    }

    let left = i + 1;
    let right = l.length - 1;

    while (left < right) {
      const sum = l[i] + l[left] + l[right];

      if (sum < 0) {
        left++;
      } else if (sum > 0) {
        right--;
      } else {
        return true;
      }
    }
  }

  return false;
};

module.exports = triplesSumToZero;

// triplesSumToZero([1, 2, 3, 7])
// triplesSumToZero([2, 4, -5, 3, 9, 7])
// triplesSumToZero([1])
// triplesSumToZero([1, 3, -2, 1])
// triplesSumToZero([1, 3, 5, 0])
// triplesSumToZero([-1, -1, 2])
// triplesSumToZero([-1, 0, 1, 2, -1, -4])
// triplesSumToZero([-1, -1, -1, -1, 2])
// triplesSumToZero([-2, 0, 0, 2, 2])
// triplesSumToZero([-2, 0, 1, 1, 2])
// triplesSumToZero([-3, 0, 1, 2, -1, 1, 1])
// triplesSumToZero([-3, 0, 0, 0])
// triplesSumToZero([-3, 1, 1, 2, -2, 0, 2])
// triplesSumToZero([-3, 0, 1, 3, -1,