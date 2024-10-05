  return arr.filter(num => {
    let sum = 0;
    let strNum = num.toString();
    for (let i = 0; i < strNum.length; i++) {
      if (strNum[i] !== '-') {
        sum += Number(strNum[i]);
      }
    }
    return sum > 0;
  }).length;
}



