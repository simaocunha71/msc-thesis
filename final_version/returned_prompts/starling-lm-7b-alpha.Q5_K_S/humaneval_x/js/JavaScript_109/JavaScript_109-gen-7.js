  let max_index = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[max_index]) {
      max_index = i;
    }
  }
  let temp = arr.shift();
  arr.push(temp);
  return arr.slice(0, max_index).every((v, i) => v <= arr[i + 1]) && 
    arr.slice(max_index + 1).every((v, i) => v <= arr[i]);
}



