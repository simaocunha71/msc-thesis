  var result = [];
  var current_max = numbers[0];
  for (const num of numbers) {
    if (num > current_max) {
      current_max = num;
    }
    result.push(current_max);
  }
  return result;
}



