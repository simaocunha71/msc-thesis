  let count = 0;
  for (const num of nums) {
    let strNum = num.toString();
    let firstDigit = strNum[0];
    let lastDigit = strNum[strNum.length - 1];
    if (firstDigit % 2 !== 0 && lastDigit % 2 !== 0 && num > 10) {
      count += 1;
    }
  }
  return count;
}



