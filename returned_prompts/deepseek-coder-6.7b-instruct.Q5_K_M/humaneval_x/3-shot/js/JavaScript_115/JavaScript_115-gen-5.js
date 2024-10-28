  let count = Array.from({length: grid[0].length}, () => 0);
  let total_steps = 0;

  for  (let row of grid) {
    for  (let i in row) {
      if  (row[i] == 1) {
        count[i]++;
      }
    }
  }

  count.sort((a, b) => a - b);

  let l = 0;
  let r = count.length - 1;

  while  (l <= r) {
    if  (count[l] + count[r] < capacity) {
      total_steps += count[r--];
    } else {
      total_steps += (capacity - count[l++]);
    }
  }

  return total_steps;
}



