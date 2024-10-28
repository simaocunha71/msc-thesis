  var test_list = test.split(' ');
  var test_dict = {};
  var max_value = -1;
  var max_key = '';

  for (let i = 0; i < test_list.length; i++) {
    if (test_dict.hasOwnProperty(test_list[i])) {
      test_dict[test_list[i]] += 1;
    } else {
      test_dict[test_list[i]] = 1;
    }
  }

  for (const key in test_dict) {
    if (test_dict[key] > max_value) {
      max_value = test_dict[key];
      max_key = key;
    }
  }

  if (max_value == -1) {
    return {};
  } else if (test_dict[max_key] == 1) {
    return {max_key};
  } else {
    return {max_key: max_value};
  }
}



