  let total = 0;
  let numbers = s.split(" ").map(num => {
    return parseInt(num.split(" ")[1]);
  });
  for (const num of numbers) {
    total += num;
  }
  return n - total;
}



