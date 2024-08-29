  let result = {};
  for (const c of test.split(' ')) {
    if (result[c] === undefined) {
      result[c] = 0;
    }
    result[c] += 1;
  }

  let max_value = 0;
  let max_keys = [];
  for (const key in result) {
    if (result[key] > max_value) {
      max_value = result[key];
      max_keys = [key];
    } else if (result[key] == max_value) {
      max_keys.push(key);
    }
  }

  if (max_value == 0) {
    return {};
  } else if (max_value == 1) {
    return max_keys[0];
  } else {
    return max_keys;
  }
}



