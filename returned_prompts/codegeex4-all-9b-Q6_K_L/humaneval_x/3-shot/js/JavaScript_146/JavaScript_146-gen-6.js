  var count = 0;
  for (let num of nums) {
    if (num > 10 && num % 2 == 1) {
      var strNum = num.toString();
      if (strNum[0] % 2 == 1 && strNum[strNum.length - 1] % 2 == 1) {
        count++;
      }
    }
  }
  return count;
}