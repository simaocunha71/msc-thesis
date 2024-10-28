  var result = 0;
  var num_string = N.toString(2);
  for (const c of num_string) {
    if (c == '1') {
      result += 1;
    }
  }
  return result.toString(2);
}



