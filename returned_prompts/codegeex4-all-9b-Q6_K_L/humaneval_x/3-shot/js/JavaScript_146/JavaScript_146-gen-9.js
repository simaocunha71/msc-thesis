  let count = 0;
  for (let num of nums) {
    if (num > 10 && num % 2 == 1 && num.toString()[0] % 2 == 1 && num.toString()[num.toString().length - 1] % 2 == 1) {
      count++;
    }
  }
  return count;
}



