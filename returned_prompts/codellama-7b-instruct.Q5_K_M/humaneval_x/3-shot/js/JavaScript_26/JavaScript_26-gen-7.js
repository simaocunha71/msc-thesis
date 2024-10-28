  var result = [];
  var seen = {};

  for (const num of numbers) {
    if (!(num in seen)) {
      seen[num] = 1;
      result.push(num);
    }
  }

  return result;
}



