  for (let i = 0; i < arr.length; i++) {
    let sorted = true;
    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        sorted = false;
        break;
      }
    }
    if (sorted) {
      return true;
    }
    arr.push(arr.shift());
  }
  return false;
}


