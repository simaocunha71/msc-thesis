const canArrange = (arr) => {
  let maxIndex = -1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[i - 1]) {
      maxIndex = i;
    }
  }
  return maxIndex;
}

// T: O(n)
// S: O(1)

/*
  