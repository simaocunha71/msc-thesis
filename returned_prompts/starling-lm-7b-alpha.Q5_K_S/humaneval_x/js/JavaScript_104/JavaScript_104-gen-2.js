  let result = [];
  let sorted_x = [...x].sort((a, b) => a - b);

  for (const i of sorted_x) {
    if (i.toString().split('').filter(n => n % 2 == 0).length == 0) {
      result.push(i);
    }
  }

  return result.sort((a, b) => a - b);
}



