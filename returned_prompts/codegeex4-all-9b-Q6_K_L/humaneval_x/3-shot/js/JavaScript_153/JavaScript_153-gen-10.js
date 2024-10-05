  var strongestExtension = "";
  var strongestExtensionStrength = 0;

  for (const extension of extensions) {
    var strength = 0;
    for (const c of extension) {
      if (c == c.toUpperCase()) {
        strength += 1;
      } else {
        strength -= 1;
      }
    }
    if (strength > strongestExtensionStrength) {
      strongestExtension = extension;
      strongestExtensionStrength = strength;
    }
  }

  return class_name + "." + strongestExtension;
}



