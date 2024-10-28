  var strongest_extension_name = null;
  var strongest_extension_strength = 0;

  for (const extension_name of extensions) {
    let strength = 0;
    for (const c of extension_name) {
      if (c >= 'A' && c <= 'Z') {
        strength -= 1;
      } else if (c >= 'a' && c <= 'z') {
        strength += 1;
      }
    }
    if (strength > strongest_extension_strength) {
      strongest_extension_strength = strength;
      strongest_extension_name = extension_name;
    }
  }

  return class_name + '.' + strongest_extension_name;
}



