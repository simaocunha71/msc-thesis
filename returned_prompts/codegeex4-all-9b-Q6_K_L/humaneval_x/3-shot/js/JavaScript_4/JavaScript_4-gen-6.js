  var sum = 0;
  var avg = 0;
  var deviation = 0;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  avg = sum / numbers.length;

  for (let i = 0; i < numbers.length; i++) {
    deviation += Math.abs(numbers[i] - avg);
  }
  deviation /= numbers.length;

  return deviation;
}



