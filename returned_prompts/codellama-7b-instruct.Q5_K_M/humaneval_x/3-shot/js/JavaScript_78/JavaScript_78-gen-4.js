  var prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
  var result = 0;

  for (var i = 0; i < num.length; i++) {
    if (prime_numbers.indexOf(parseInt(num[i], 16)) != -1) {
      result += 1;
    }
  }

  return result;
}



