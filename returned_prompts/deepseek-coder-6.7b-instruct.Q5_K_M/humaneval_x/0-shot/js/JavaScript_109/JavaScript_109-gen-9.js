  if(arr.length === 0)
    return true;

  let sortedArray = [...arr].sort((a, b) => a - b);
  let shiftedArray = [...arr.slice(1), arr[0]];

  while(shiftedArray[0] !== sortedArray[0]){
    if(shiftedArray[0] === sortedArray[1])
      return true;
    shiftedArray = [shiftedArray[0], ...shiftedArray.slice(1), shiftedArray.slice(1)[0]];
  }

  return false;
}

console.log(moveOneBall([3, 4, 5, 1, 2])); // true
console.log(moveOneBall([3, 5, 4, 1, 2])); // false
console.log(moveOneBall([])); // true

*/

/*
