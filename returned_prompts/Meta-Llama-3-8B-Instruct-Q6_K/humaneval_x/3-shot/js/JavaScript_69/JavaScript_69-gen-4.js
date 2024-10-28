  let max = 0;
  let maxCount = 0;
  let countMap = {};

  for (let i = 0; i < lst.length; i++) {
    let num = lst[i];
    if (countMap[num] === undefined) {
      countMap[num] = 1;
    } else {
      countMap[num]++;
    }
    if (num > max && countMap[num] >= num) {
      max = num;
      maxCount = countMap[num];
    }
  }

  if (maxCount < max) {
    return -1;
  }

  return max;
}