  var max_strength = -Infinity;
  var max_strength_extension = '';
  for (const extension of extensions) {
    var strength = 0;
    for (const c of extension) {
      if (c == c.toUpperCase()) {
        strength += 1;
      } else {
        strength -= 1;
      }
    }
    if (strength > max_strength) {
      max_strength = strength;
      max_strength_extension = extension;
    }
  }
  return `${class_name}.${max_strength_extension}`;
}