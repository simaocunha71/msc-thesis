  let sorted = arr.slice().sort((a, b) => a - b);
  let rotated = sorted.shift();
  sorted.push(rotated);
  return arr.every((num, i) => num == sorted[i]);
}