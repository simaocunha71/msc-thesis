  var strongest_extension = "";
  var strongest_strength = -1;

  for (var extension of extensions) {
    var strength = 0;
    for (var c of extension) {
      if (c.toUpperCase() == c) {
        strength += 1;
      } else {
        strength -= 1;
      }
    }
    if (strength > strongest_strength) {
      strongest_strength = strength;
      strongest_extension = extension;
    }
  }

  return class_name + '.' + strongest_extension;
}



