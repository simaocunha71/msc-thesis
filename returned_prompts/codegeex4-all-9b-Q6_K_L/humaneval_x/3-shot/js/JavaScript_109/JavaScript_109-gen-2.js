  var sorted_arr = arr.slice().sort((a, b) => a - b);
  var rotated_arr = sorted_arr.slice(1).concat(sorted_arr[0]);
  return JSON.stringify(rotated_arr) === JSON.stringify(arr);
}



