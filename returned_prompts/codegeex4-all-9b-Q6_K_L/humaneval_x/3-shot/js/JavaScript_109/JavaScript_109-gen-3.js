  var sorted = arr.slice().sort((a, b) => a - b);
  var shifted = arr.slice(1).concat(arr[0]);
  return JSON.stringify(sorted) === JSON.stringify(shifted);
}