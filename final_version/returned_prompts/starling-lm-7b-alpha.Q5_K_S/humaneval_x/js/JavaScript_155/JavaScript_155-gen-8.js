  let count = [0, 0];
  while (num != 0) {
    count[num % 2] += 1;
    num = Math.floor(num / 10);
  }
  return count;
}



