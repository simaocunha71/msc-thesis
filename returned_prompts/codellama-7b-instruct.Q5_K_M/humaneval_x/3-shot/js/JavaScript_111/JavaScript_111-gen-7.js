  var test_list = test.split(" ");
  var letter_count = {};

  for (var i = 0; i < test_list.length; i++) {
    if (letter_count[test_list[i]] == undefined) {
      letter_count[test_list[i]] = 1;
    }
    else {
      letter_count[test_list[i]] += 1;
    }
  }

  return letter_count;
}



