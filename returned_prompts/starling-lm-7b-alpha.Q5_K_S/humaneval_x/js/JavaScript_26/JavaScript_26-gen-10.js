  let result = [];
  let used = {};
  for (let i = 0; i < numbers.length; i++) {
    if (!used[numbers[i]]) {
      used[numbers[i]] = true;
      result.push(numbers[i]);
    }
  }
  return result;
}



