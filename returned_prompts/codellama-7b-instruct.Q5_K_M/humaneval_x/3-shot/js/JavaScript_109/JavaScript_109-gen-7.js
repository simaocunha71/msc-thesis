  if (arr.length == 0) {
    return true;
  }

  let sorted = arr.slice().sort((a, b) => a - b);

  let current = arr.slice();
  let i = 0;

  while (i < arr.length) {
    if (current[i] != sorted[i]) {
      let j = 0;
      while (current[i] != sorted[j]) {
        j++;
      }

      if (j == arr.length - 1) {
        return false;
      }

      let k = j;
      while (k < arr.length - 1) {
        let temp = current[k];
        current[k] = current[k + 1];
        current[k + 1] = temp;
        k++;
      }

      current[k] = sorted[j];
    }

    i++;
  }

  return true;
}



