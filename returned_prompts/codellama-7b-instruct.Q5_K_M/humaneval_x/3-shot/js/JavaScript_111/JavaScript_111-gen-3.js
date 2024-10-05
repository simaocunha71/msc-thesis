  var test_list = test.split(' ');
  var test_dict = {};

  for (var i = 0; i < test_list.length; i++) {
    if (test_dict[test_list[i]] == undefined) {
      test_dict[test_list[i]] = 1;
    } else {
      test_dict[test_list[i]] += 1;
    }
  }

  return test_dict;
}



