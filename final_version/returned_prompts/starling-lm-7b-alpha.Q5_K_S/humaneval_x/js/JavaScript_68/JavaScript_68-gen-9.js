  let result = [];
  let even = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      even.push([arr[i], i]);
    }
  }
  if (even.length > 0) {
    result = even.sort((a, b) => a[0] - b[0]);
    result = result[0];
  }
  return result;
}



