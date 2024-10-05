  let smallest = Number.MAX_SAFE_INTEGER;
  let smallest_index = -1;

  for (let i = 0; i < arr.length; i++) {
    let num = arr[i];
    if (num % 2 == 0 && num < smallest) {
      smallest = num;
      smallest_index = i;
    }
  }

  if (smallest_index == -1) {
    return [];
  } else {
    arr.splice(smallest_index, 1);
    return [smallest, smallest_index];
  }
}



