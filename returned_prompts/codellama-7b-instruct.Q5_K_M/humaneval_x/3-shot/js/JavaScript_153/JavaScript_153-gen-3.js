  var strongest_extension = '';
  var strongest_strength = 0;

  for (let extension of extensions) {
    let extension_strength = 0;
    for (let c of extension) {
      if (c.toUpperCase() == c) {
        extension_strength += 1;
      } else {
        extension_strength -= 1;
      }
    }
    if (extension_strength > strongest_strength ||
      (extension_strength == strongest_strength &&
        extension < strongest_extension)) {
      strongest_extension = extension;
      strongest_strength = extension_strength;
    }
  }

  return class_name + '.' + strongest_extension;
}



