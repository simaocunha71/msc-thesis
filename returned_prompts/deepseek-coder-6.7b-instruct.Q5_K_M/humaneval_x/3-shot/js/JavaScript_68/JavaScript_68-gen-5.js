  let smallest_even = {value: Infinity, index: -1};

  for  (let i = 0; i < arr.length; i++) {
    if  (arr[i] < smallest_even.value  && arr[i] % 2 === 0) {
      smallest_even = {value: arr[i], index: i};
    }
  }

  return smallest_even.index === -1 ? [] : [smallest_even.value, smallest_even.index];
}



