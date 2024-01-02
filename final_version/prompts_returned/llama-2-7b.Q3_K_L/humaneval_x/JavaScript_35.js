/*Return maximum element in the list.
  >>> maxElement([1, 2, 3])
  3
  >>> maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
  123
  */
const maxElement = (l) => {
  let n = l.length;
  if(n === 1){ // if there is only one element in list
    return l[0];
  } else {
    let k = 0,
        tempMax = -Infinity;
    for (let i = 0; i < n; i++) { // looping over all elements to find max
      if(l[i] > tempMax){ // updating the previous maximum
        tempMax = l[i];
        k = i;
      }
      console.log(`${tempMax} `);
    }
    return l[k];
  }
};
console.log("maxElement([1, 2, 3])", maxElement([1, 2, 3])); // 3
