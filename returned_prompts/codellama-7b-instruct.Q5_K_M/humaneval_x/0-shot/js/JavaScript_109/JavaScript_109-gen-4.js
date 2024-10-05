/*
  In the worst case, we need to do N - 1 comparisons to find the minimum
  element and move it to the first position. In the worst case, we need to do 
  N - 1 comparisons to find the maximum element and move it to the last position.
  So, the total time complexity of the algorithm is O(N).
  */
const moveOneBall = (arr) => {
  const len = arr.length;
  if (len === 0) return true;

  const min = arr.indexOf(Math.min(...arr));
  const max = arr.indexOf(Math.max(...arr));

  if (min === max) return true;

  if (min > max) {
    arr.splice(max, 1);
    arr.unshift(arr[len - 1]);
    arr.splice(len - 1, 1);
  } else {
    arr.splice(min, 1);
    arr.push(arr[0]);
    arr.splice(0, 1);
  }
  return moveOneBall(arr);
}
