  let count = 0;
  
  for(let i = 0; i < arr.length; i++){
    let sum = 0;
    let strNum = String(Math.abs(arr[i]));
    
    for(let j = 0; j < strNum.length; j++){
      sum += Number(strNum[j]);
    }
    
    if(arr[i] < 0){
      sum *= -1;
    }
    
    if(sum > 0){
      count++;
    }
  }
  
  return count;
}

console.log(countNums([])); // 0
console.log(countNums([-1, 11, -11])); // 1
console.log(countNums([1, 1, 2])); // 3

*/

// Your code goes here

/*
