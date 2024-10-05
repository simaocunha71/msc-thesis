  var min_val = numbers[0];
  var max_val = numbers[0];

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < min_val) {
      min_val = numbers[i];
    } else if (numbers[i] > max_val) {
      max_val = numbers[i];
    }
  }

  var rescaled_list = [];
  for (let i = 0; i < numbers.length; i++) {
    rescaled_list.push((numbers[i] - min_val) / (max_val - min_val));
  }

  return rescaled_list;
}



