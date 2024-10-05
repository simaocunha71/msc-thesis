  var result = [];
  for (var i = 0; i < x.length; i++) {
    var tmp = x[i];
    var tmp_str = tmp.toString();
    var tmp_arr = tmp_str.split('');
    var tmp_new_arr = [];
    for (var j = 0; j < tmp_arr.length; j++) {
      if (tmp_arr[j] % 2 == 1) {
        tmp_new_arr.push(tmp_arr[j]);
      }
    }
    if (tmp_new_arr.length > 0) {
      result.push(tmp);
    }
  }
  result.sort();
  return result;
}



