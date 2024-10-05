/*
  This solution is similar to the previous one, but it is a bit more elegant.
  The idea is to find the largest number in the array and then to find the
  smallest number in the array. We then check if the difference between the
  largest and smallest is even, and if it is, we can add half of that difference
  to the largest number to make it palindromic.
*/
const smallestChange = (arr) => {
  let largest = arr[0];
  let smallest = arr[0];

  for (let i = 1; i < arr.length; i++) {
    largest = Math.max(arr[i], largest);
    smallest = Math.min(arr[i], smallest);
  }

  if (largest - smallest % 2 === 0) {
    return (largest + smallest) / 2;
  }
  return largest - smallest;
};

