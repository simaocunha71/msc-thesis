  if (arr.length === 0 || arr.slice().sort((a, b) => a - b).every((v, i) => v === arr[i])) {
    return true;
  }

  for