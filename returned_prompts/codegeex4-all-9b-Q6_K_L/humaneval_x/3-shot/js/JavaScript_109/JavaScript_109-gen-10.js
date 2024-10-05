  let sortedArray = arr.sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== sortedArray[i]) {
      return false;
    }
  }
  return true;
}



