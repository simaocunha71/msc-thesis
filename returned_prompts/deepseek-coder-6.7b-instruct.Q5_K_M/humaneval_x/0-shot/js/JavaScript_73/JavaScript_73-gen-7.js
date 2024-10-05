  let count = 0;
  for(let i = 0; i < arr.length; i++){
    for(let j = i + 1; j < arr.length; j++){
      if(Math.abs(arr[i] - arr[j]) === k){
        count++;
      }
    }
  }
  return count;
}

console.log(pairs([1, 7, 5, 9, 2, 12, 3], 2)); // 3
console.log(pairs([1, 3, 5, 7], 1)); // 1
console.log(pairs([1, 3, 5, 7], 2)); // 2
*/

/*
  Given an array of integers, find the number of pairs of elements that have a difference equal to a given number k.

  For example:
  pairs([1, 7, 5, 9, 2, 12,