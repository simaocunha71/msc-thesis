/*"
  The function uses two variables to keep track of the sum of the squared and cubed entries. It uses a for-loop to iterate over the 
  list, using the index of the list entry as a multiple of 3 and 4 to determine whether to square or cube the value, and whether 
  to add the value to the sum. 
  */
  const sumSquares = (lst) => {
    let squaredSum = 0;
    let cubedSum = 0;
    for(let i = 0; i < lst.length; i++) {
      if(i % 3 === 0) {
        squaredSum += lst[i] * lst[i];
      } else if(i % 4 === 0 && i % 3 !== 0) {
        cubedSum += lst[i] * lst[i] * lst[i];
      }
    }
    return squaredSum + cubedSum;
  };
}
