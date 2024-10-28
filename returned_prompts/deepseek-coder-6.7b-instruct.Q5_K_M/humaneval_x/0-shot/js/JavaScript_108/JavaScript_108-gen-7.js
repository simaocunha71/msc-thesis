  let count = 0;
  
  for(let i = 0; i < arr.length; i++) {
    let sum = 0;
    let str = String(arr[i]);
    for(let j = 0; j < str.length; j++) {
      sum += Number(str[j]);
    }
    if (sum === 0) {
      count++;
    }
  }

  return count;
}

console.log(countNums([]) == 0);
console.log(count