  var test_list = test.split(" ");
  var result = {};
  var max = 0;
  var max_list = [];

  for (var i = 0; i < test_list.length; i++) {
    if (result[test_list[i]] == undefined) {
      result[test_list[i]] = 1;
    } else {
      result[test_list[i]] += 1;
    }

    if (result[test_list[i]] == max) {
      max_list.push(test_list[i]);
    } else if (result[test_list[i]] > max) {
      max = result[test_list[i]];
      max_list = [];
      max_list.push(test_list[i]);
    }
  }

  return { [test]: result };
}



