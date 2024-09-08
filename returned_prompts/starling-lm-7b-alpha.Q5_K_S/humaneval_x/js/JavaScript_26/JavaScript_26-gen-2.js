  let result = [];
  let seen = {};
  for (let i = 0; i < numbers.length; i++) {
    if (!seen[numbers[i]]) {
      seen[numbers[i]] = true;
      result.push(numbers[i]);
    }
  }
  return result;
}



