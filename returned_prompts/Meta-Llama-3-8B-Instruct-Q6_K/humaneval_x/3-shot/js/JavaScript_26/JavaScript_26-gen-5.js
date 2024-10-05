  var result = [];
  var seen = {};

  for (var i = 0; i < numbers.length; i++) {
    var num = numbers[i];
    if (!seen[num]) {
      result.push(num);
      seen[num] = true;
    }
  }

  return result;
}...



