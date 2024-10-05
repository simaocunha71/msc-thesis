  let smallestEven = Number.MAX_SAFE_INTEGER;
  let smallestEvenIndex = -1;

  for (let i = 0; i < arr.length; i++) {
    let value = arr[i];

    if (value % 2 == 0 && value < smallestEven) {
      smallestEven = value;
      smallestEvenIndex = i;
    }
  }

  if (smallestEvenIndex == -1) {
    return [];
  } else {
    return [smallestEven, smallestEvenIndex];
  }
}