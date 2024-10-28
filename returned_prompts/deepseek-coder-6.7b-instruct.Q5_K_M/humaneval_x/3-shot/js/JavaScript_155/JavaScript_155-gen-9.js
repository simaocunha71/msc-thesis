  let evenCount = 0, oddCount = 0;
  let numArr = Math.abs(num).toString().split('');
  
  numArr.forEach(n => (n % 2 == 0) ? evenCount++ : oddCount++);
  
  return [evenCount, oddCount];
}



