  let count = 0;
  arr.forEach(num => {
    let sum = 0;
    let strNum = num.toString();
    for(let i = 0; i < strNum.length; i++) {
      sum += parseInt(strNum[i]);
    }
    if(sum > 0) {
      count++;
    }
  })
  return count;
}



