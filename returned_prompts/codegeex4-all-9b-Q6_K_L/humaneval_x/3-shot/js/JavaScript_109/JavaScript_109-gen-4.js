  let sorted_arr = arr.slice().sort((a, b) => a - b);
  let shifted_arr = arr.slice(1).concat(arr[0]);
  return JSON.stringify(sorted_arr) === JSON.stringify(shifted_arr);
}

