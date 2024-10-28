  var result = {};
  var string_array = test.split(' ');

  for (var i = 0; i < string_array.length; i++) {
    if (result[string_array[i]] === undefined) {
      result[string_array[i]] = 1;
    } else {
      result[string_array[i]] += 1;
    }
  }

  return result;
}



