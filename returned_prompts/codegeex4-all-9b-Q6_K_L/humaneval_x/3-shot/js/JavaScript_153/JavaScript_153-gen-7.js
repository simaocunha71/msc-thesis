  var strongest_extension = null;
  var strongest_strength = -Infinity;

  for (const extension of extensions) {
    var strength = 0;
    for (const c of extension) {
      if (c == c.toUpperCase()) {
        strength += 1;
      } else {
        strength -= 1;
      }
    }
    if (strength > strongest_strength) {
      strongest_extension = extension;
      strongest_strength = strength;
    }
  }

  return class_name + '.' + strongest_extension;
}