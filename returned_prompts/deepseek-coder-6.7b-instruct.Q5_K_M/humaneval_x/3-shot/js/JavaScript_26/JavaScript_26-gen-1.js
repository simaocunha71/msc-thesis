  let result = [];
  let counts = {};

  for (let num of numbers) {
    if (counts[num]) {
      counts[num]++;
    } else {
      counts[num] = 1;
      result.push(num);
    }
  }

  return result;
}



