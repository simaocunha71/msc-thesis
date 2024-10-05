  var result = [];
  var counts = {};

  for (let n of numbers) {
    if (counts[n]) {
      counts[n]++;
    } else {
      counts[n] = 1;
    }
  }

  for (let n of numbers) {
    if (counts[n] === 1) {
      result.push(n);
    }
  }

  return result;
}



