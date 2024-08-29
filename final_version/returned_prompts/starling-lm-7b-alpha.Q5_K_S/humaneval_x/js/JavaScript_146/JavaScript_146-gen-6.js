  let result = 0;
  for(const num of nums) {
    let first = Math.floor(num / 10).toString()[0];
    let last = num % 10;
    if(first != '0' && last % 2 == 1 && num > 10) {
      result += 1;
    }
  }
  return result;
}



