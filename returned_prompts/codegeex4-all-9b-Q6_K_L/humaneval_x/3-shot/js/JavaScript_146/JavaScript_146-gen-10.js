  let count = 0;

  for (let num of nums) {
    if (num > 10) {
      let strNum = num.toString();
      let firstDigit = parseInt(strNum[0]);
      let lastDigit = parseInt(strNum[strNum.length - 1]);

      if (firstDigit % 2 == 1 && lastDigit % 2 == 1) {
        count += 1;
      }
    }
  }

  return count;
}