let sum = 0;
  for (let i = 1; i < lst.length; i += 2) {
    if (lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
}

// function add(lst) {
//   let sum = 0;
//   for (let i = 1; i < lst.length; i += 2) {
//     if (lst[i] % 2 === 0) {
//       sum += lst[i];
//     }
//   }
//   return sum;
// }
console.log(add([4, 2, 6, 7])); // 2
console.log(add([1, 2, 3, 4, 5])); // 6
console.log(add([9, 2, 8, 3, 7])); // 10
console.log(add([3, 2, 1, 4, 5])); // 0
//Expected Output: 2, 6, 10, 0






//function add(lst) {
//  let sum = 0;
//  for (let i = 1; i < lst.length; i += 2) {
//    if (lst[i] % 2 === 0) {
//      sum += lst[i];
//    }
//  }
//  return sum;
//}
//console.log(add([4, 2, 6, 7])); // 2
//console.log(add([1, 2, 3, 4, 5])); // 6
//console.log(add([9, 2, 8, 3, 7])); // 10
//console.log(add([3, 2, 1, 4, 5])); // 0
//Expected Output: 2, 6, 10, 0
