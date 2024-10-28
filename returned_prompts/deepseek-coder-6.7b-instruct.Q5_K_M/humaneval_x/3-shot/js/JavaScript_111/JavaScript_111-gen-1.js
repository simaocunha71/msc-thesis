  const count = {};
  const words = test.split(' ');
  for (const word of words) {
    count[word] = (count[word] || 0) + 1;
  }
  let maxCount = 0;
  for (const key in count) {
    if (count[key] > maxCount) {
      maxCount = count[key];
    }
  }
  const result = {};
  for (const key in count) {
    if (count[key] === maxCount) {
      result[key] = count[key];
    }
  }
  return result;
}



