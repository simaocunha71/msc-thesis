  let result = {};
  let words = test.split(' ');
  for (let word of words) {
    if (result[word] == undefined) {
      result[word] = 1;
    } else {
      result[word] += 1;
    }
  }
  return result;
}