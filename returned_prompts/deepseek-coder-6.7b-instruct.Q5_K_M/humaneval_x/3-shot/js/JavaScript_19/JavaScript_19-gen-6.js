  var numbersArray = numbers.split(" ");
  var numbersMap = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 };

  numbersArray.sort(function(a, b) {
    return numbersMap[a] - numbersMap[b];
  });

  return numbersArray.join(" ");
}



