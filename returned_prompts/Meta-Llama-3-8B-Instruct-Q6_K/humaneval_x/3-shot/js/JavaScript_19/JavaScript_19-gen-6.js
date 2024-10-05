  var numbers_list = numbers.split(' ');
  numbers_list.sort(function(a, b) {
    var a_value = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[a];
    var b_value = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[b];
    return a_value - b_value;
  });
  return numbers_list.join(' ');
}