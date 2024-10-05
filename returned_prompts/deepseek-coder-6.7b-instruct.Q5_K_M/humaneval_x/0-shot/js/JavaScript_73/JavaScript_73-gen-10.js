  let changes = 0;
  for(let i = 0; i < Math.floor(arr.length / 2); i++){
    if(arr[i] !== arr[arr.length - 1 - i]){
      changes++;
    }
  }
  return changes;
}

console.log(smallestChange([1,2,3,5,4,7,9,6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0

*/



// JavaScript solution:

function smallestChange(arr) {
    let changes = 0;
    for(let i = 0; i < Math.floor(arr.length / 2); i++){
      if(arr[i] !== arr[arr.length - 1 - i]){
        changes++;
      }
    }
    return changes;
}

console.log(smallestChange([1,2,3,5,4,7,9,6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0

/*
In this solution, we iterate over the first half of the array and compare each element to its corresponding element from the end of the array. If these two elements are not equal, we increment the counter of changes. Finally, we return the number of changes.
*/













































































































