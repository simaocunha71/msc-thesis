  let result = {};
  for (const c of test.split(' ')) {
    if (!result[c]) {
      result[c] = 0;
    }
    result[c] += 1;
  }
  let max = 0;
  let max_keys = [];
  for (let key in result) {
    if (result[key] > max) {
      max = result[key];
      max_keys = [key];
    } else if (result[key] == max) {
      max_keys.push(key);
    }
  }
  return max_keys.length == 1 ? [max_keys[0]] : max_keys;
}



