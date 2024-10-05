  var min = Math.min.apply(Math, numbers);
  var max = Math.max.apply(Math, numbers);

  return numbers.map(x => (x - min) / (max - min));
}



