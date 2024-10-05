  if(arr.length === 0) return null;

  let sum = 0;
  let signProduct = 1;

  for(let num of arr){
    if(num === 0) return 0;
    else if(num > 0) signProduct *= 1;
    else if(num < 0){
      signProduct *= -1;
      num *= -1;
    }
    sum += num;
  }

  return signProduct * sum;
}



