  let smallestEven = Infinity;
  let smallestIndex = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallestEven) {
      smallestEven = arr[i];
      smallestIndex = i;
    }
  }
  if (smallestEven === Infinity) {
    return [];
  }
  return [smallestEven, smallestIndex];
}