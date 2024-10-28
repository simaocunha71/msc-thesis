  const arr = [4, 2, 3];
  const result = [];

  for(let i = 0; i < arr.length; i++) {
    if(arr[i] % 2 === 0) {
      if(result.length === 0 || result[0] > arr[i]) {
        result[0] = arr[i];
        result[1] = i;
      }
    }
  }

  return result;
};

const result = pluck(arr);
console.log(result);
