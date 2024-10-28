  return arr.reduce((count, num) => {
    if (num.toString().split('').reduce((sum, digit) => sum + (digit === '-' ? -1 : +digit), 0) > 0) {
      count++;
    }
    return count;
  }, 0);
}



