  var result = 0;
  for (const num of lst) {
    if (num % 1 == 0 && num > 0) {
      result += num * num;
    }
  }
  return result;
}



