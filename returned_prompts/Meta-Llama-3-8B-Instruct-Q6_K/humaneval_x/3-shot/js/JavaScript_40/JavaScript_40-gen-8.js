  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      for (let k = j + 1; k < l.length; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          return true;
        }
      }
    }
  }
  return false;
}
// or using Set
const triplesSumToZero = (l) => {
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      for (let k = j + 1; k < l.length; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          return true;
        }
      }
    }
  }
  return false;
}
// or using sort and two pointers
const triplesSumToZero = (l) => {
  l.sort((a, b) => a - b);
  for (let i = 0; i < l.length - 2; i++) {
    let left = i + 1;
    let right = l.length - 1;
    while (left < right) {
      let sum = l[i] + l[left] + l[right];
      if (sum === 0) {
        return true;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return false;
}