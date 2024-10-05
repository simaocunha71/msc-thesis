  var max = -10;
  var max_name = '';
  for (const name of extensions) {
    var CAP = 0;
    var SM = 0;
    for (const c of name) {
      if (c == c.toUpperCase()) {
        CAP += 1;
      } else {
        SM += 1;
      }
    }
    var strength = CAP - SM;
    if (strength > max) {
      max = strength;
      max_name = name;
    }
  }

  return class_name + '.' + max_name;
}