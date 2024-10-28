  if (arr.length === 0) return true;

  let rightShifts = 0;

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      rightShifts++;
    }
  }

  if (arr[arr.length - 1] > arr[0]) {
    rightShifts++;
  }

  return rightShifts <= 1;
}



