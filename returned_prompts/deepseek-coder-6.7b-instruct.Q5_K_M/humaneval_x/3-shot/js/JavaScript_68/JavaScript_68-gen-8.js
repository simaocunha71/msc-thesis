  let smallestEven = Infinity;
  let smallestEvenIndex = -1;

  for  (let i = 0; i < arr.length; i++) {
    if (arr[i] < smallestEven && arr[i] % 2 === 0) {
      smallestEven = arr[i];
      smallestEvenIndex = i;
    }
  }

  return smallestEvenIndex !== -1 ? [smallestEven, smallestEvenIndex] : [];
}



