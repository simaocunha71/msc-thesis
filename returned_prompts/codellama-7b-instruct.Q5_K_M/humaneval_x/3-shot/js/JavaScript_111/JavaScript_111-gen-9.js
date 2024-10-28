  var test_list = test.split(' ');
  var test_dict = {};
  var max_key = '';
  var max_value = 0;

  for (const t of test_list) {
    if (t in test_dict) {
      test_dict[t] += 1;
    } else {
      test_dict[t] = 1;
    }
  }

  for (const [key, value] of Object.entries(test_dict)) {
    if (value > max_value) {
      max_value = value;
      max_key = key;
    }
  }

  if (max_key == '') {
    return {};
  }

  var result_dict = {};
  result_dict[max_key] = max_value;

  for (const [key, value] of Object.entries(test_dict)) {
    if (key != max_key && value == max_value) {
      result_dict[key] = max_value;
    }
  }
  return result_dict;
}



