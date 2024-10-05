  let smallestEvenValue = Infinity;
  let smallestEvenIndex = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < smallestEvenValue && arr[i] % 2 === 0) {
      smallestEvenValue = arr[i];
      smallestEvenIndex = i;
    }
  }

  return smallestEvenIndex !== -1 ? [smallestEvenValue, smallestEvenIndex] : [];
}



