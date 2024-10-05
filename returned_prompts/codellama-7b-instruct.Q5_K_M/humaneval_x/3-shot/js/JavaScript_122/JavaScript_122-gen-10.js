  var sum = 0;

  for (const num of arr.slice(0, k)) {
    if (num < 100) {
      sum += num;
    }
  }

  return sum;
}



