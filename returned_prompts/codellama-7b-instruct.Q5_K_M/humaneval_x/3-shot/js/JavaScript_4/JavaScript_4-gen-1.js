  var mean = meanOf(numbers);
  var sum = 0.0;

  for (let i of numbers) {
    sum += Math.abs(i - mean);
  }

  return sum / numbers.length;
}



