const strangeSortList = (lst) => {
  // return an empty array if the input is empty
  if (lst.length === 0) return [];

  // create a copy of the input array
  let arr = lst.slice();

  // sort the copy in ascending order
  arr.sort((a, b) => a - b);

  // create a new array to store the result
  let result = [];

  // use a boolean flag to determine whether to add the minimum or maximum
  let addMin = true;

  // loop until the copy is empty
  while (arr.length > 0) {
    // if addMin is true, add the minimum to the result
    if (addMin) {
      result.push(arr.shift());
    } else {
      // if addMin is false, add the maximum to the result
      result.push(arr.pop());
    }
    // toggle the addMin flag
    addMin = !addMin;
  }

  // return the result
  return result;
};