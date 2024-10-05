  var result = [];
  var num = a;

  while (num <= b) {
    if (num % 2 == 0) {
      result.push(num);
    }
    num += 1;
  }

  return result;
}



