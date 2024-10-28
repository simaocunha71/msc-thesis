  let set = new Set();
  let result = [];
  for (let i = 0; i < numbers.length; i++) {
    if (!set.has(numbers[i])) {
      set.add(numbers[i]);
      result.push(numbers[i]);
    }
  }
  return result;
}