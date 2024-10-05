  var result = 0.0;

  for (var i = 0; i < lst.length; i++) {
    var current = lst[i];
    if (current % 1 == 0 && current >= 0) {
      if (current % 2 == 1) {
        result += Math.pow(current, 2);
      }
    }
  }

  return result;
}



