  var min = Math.min(...numbers);
  var max = Math.max(...numbers);

  return numbers.map(x => (x - min) / (max - min));
}