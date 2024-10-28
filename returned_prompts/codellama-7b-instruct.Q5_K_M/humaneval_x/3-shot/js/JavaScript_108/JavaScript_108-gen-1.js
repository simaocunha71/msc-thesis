  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    let num = arr[i];

    for (let j = 0; j < num.toString().length; j++) {
      sum += parseInt(num.toString()[j]);
    }

    if (sum > 0) count++;
  }

  return count;
}



