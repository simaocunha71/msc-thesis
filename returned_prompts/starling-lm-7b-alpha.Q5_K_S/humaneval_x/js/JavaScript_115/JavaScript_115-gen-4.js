  let count = 0;
  while (true) {
    let filled = false;
    for (let i = 0; i < grid.length; i++) {
      let sum = 0;
      for (let j = 0; j < grid[i].length; j++) {
        sum += grid[i][j];
      }
      if (sum != 0) {
        filled = true;
        grid[i] = grid[i].map(n => n % capacity);
        sum = sum % capacity;
        count += Math.ceil(sum / capacity);
      }
    }
    if (!filled) {
      break;
    }
  }
  return count;
}



