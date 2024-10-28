  var seen = {};
  var result = [];
  for (const num of numbers) {
    if (!seen[num]) {
      seen[num] = true;
      result.push(num);
    }
  }
  return result;
} 



