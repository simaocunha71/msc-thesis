  let count = 0;
  arr.forEach((num) => {
    let sum = 0;
    let strNum = String(num);
    for (let i = 0; i < strNum.length; i++) {
      sum += Number(strNum[i]);
    }
    if (sum > 0) count++;
  });
  return count;
}



