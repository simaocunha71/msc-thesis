  if(array.length === 0) return array;

  let sortedArray = array.slice().sort((a,b) => a - b);

  if((array[0] + array[array.length - 1]) % 2 !== 0) return sortedArray;

  return sortedArray.reverse();
}
*/

