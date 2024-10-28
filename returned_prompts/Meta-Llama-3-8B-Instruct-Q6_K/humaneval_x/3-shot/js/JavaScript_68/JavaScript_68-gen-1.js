  if (arr.length === 0) {
    return [];
  }

  let minEvenIndex = -1;
  let minEvenValue = Infinity;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < minEvenValue) {
      minEvenValue = arr[i];
      minEvenIndex = i;
    } else if (arr[i] % 2 === 0 && arr[i] === minEvenValue) {
      minEvenIndex = Math.min(minEvenIndex, i);
    }
  }

  if (minEvenIndex === -1) {
    return [];
  }

  return [minEvenValue, minEvenIndex];
}