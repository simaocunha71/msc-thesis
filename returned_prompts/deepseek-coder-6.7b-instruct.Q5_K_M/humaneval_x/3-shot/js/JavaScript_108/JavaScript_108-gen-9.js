  let count = 0;
  for  (let i = 0; i < arr.length; i++)  {
    let sum = 0;
    let num = arr[i];
    while  (num != 0)  {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if  (sum > 0)  {
      count++;
    }
  }
  return count;
}



