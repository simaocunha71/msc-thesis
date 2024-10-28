  let result = [];
  for (let i = 0; i < x.length; i++) {
    let isUnique = true;
    let currentNum = x[i];
    let currentNumStr = currentNum.toString();
    for (let j = 0; j < currentNumStr.length; j++) {
      let currentDigit = currentNumStr[j];
      if (currentDigit % 2 === 0) {
        isUnique = false;
        break;
      }
    }
    if (isUnique) {
      result.push(currentNum);
    }
  }
  return result;
}