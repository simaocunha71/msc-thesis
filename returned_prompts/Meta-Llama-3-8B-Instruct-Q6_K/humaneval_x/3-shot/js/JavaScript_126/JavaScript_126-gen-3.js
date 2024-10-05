  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      return false;
    }
  }
  return true;
}  // This function is not checking for duplicate numbers. It will return true even if there are duplicate numbers. To check for duplicate numbers, we need to modify this function to keep track of the count of each number. If we find a number that has a count greater than 1, we can return false. Here is the modified function:
// const isSorted = (lst) => {
//   let count = {};
//   for (let num of lst) {
//     if (count[num]) {
//       count[num]++;
//     } else {
//       count[num] = 1;
//     }
//   }
//   for (let i = 0; i < lst.length - 1; i++) {
//     if (lst[i] >= lst[i + 1]) {
//       return false;
//     }
//   }
//   return true;
// }  // This function still has a bug. It will return true if the list is sorted in descending order. We need to add a check for this as well. Here is the modified function:
// const isSorted = (lst) => {
//   let count = {};
//   for (let num of lst) {
//     if (count[num]) {
//       count[num]++;
//     } else {
//       count[num] = 1;
//     }
//   }
//   for (let i = 0; i < lst.length - 1; i++) {
//     if ((lst[i] >= lst[i + 1]) || (lst[i] <= lst[i + 1])) {
//       return false;
//     }
//   }
//   return true;
// }  // This function is still not correct. It will return true if the list has duplicate numbers. We need to add a check for this as well. Here is the modified function:
const isSorted = (lst) => {
  let count = {};
  for (let num of lst) {
    if (count[num]) {
      count[num]++;
    } else {
      count[num] = 1;
    }
  }
  for (let i = 0; i < lst.length - 1; i++) {
    if ((lst[i] >= lst[i + 1