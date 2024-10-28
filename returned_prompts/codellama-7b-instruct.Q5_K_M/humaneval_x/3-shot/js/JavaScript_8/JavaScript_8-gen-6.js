  if (int == true) {
    let sum = 0;
    for (let i = 0; i < numbers.length; i++) {
      sum += Math.floor(numbers[i]);
    }
    return [sum, 1];
  } else {
    let sum = 0;
    let product = 1;
    for (let i = 0; i < numbers.length; i++) {
      sum += numbers[i];
      product *= numbers[i];
    }
    return [sum, product];
  }
}



