  let minEvenValue = Infinity;
  let minEvenIndex = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < minEvenValue) {
      minEvenValue = arr[i];
      minEvenIndex = i;
    }
  }

  if (minEvenIndex === -1) {
    return [];
  }

  return [minEvenValue, minEvenIndex];
}