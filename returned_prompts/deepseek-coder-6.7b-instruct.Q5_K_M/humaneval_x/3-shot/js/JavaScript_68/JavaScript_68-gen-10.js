  let smallest_even = Number.MAX_SAFE_INTEGER;
  let smallest_index = -1;

  for  (let i = 0; i < arr.length; i++)  {
    if  (arr[i] < smallest_even  && arr[i] % 2 == 0)  {
      smallest_even = arr[i];
      smallest_index = i;
    }
  }

  return smallest_index != -1 ? [smallest_even, smallest_index] : [];
}



