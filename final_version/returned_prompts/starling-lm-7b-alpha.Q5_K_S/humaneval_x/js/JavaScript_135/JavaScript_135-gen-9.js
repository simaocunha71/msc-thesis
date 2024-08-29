  let max = -1;
  let index = -1;
  for(let i = 0; i < arr.length; i++) {
    if(arr[i] < arr[i-1]) {
      if(index > max) {
        max = index;
      }
      index = i;
    }
  }
  return max;
}



