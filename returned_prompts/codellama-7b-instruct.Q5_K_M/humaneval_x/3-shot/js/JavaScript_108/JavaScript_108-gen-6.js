  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    sum = 0;
    for (let j = 0; j < arr[i].toString().length; j++) {
      sum += parseInt(arr[i].toString()[j]);
    }
    if (sum > 0) {
      return arr.length;
    }
  }
  return 0;
}



