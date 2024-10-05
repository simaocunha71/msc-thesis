  if (arr.length === 0) {
    return true;
  }

  let maxIndex = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[maxIndex]) {
      maxIndex = i;
    }
  }

  for (let i = 0; i < arr.length; i++) {
    if (i !== maxIndex) {
      return false;
    }
    maxIndex = (maxIndex + 1) % arr.length;
  }

  return true;
}