  let result = class_name;
  let max_strength = 0;
  let max_extension = null;

  for (const extension of extensions) {
    let strength = 0;
    for (const c of extension) {
      if (c == c.toLowerCase()) {
        strength += 1;
      } else {
        strength -= 1;
      }
    }
    if (max_strength < strength) {
      max_strength = strength;
      max_extension = extension;
    } else if (max_strength == strength) {
      if (extensions.indexOf(max_extension) > extensions.indexOf(extension)) {
        max_extension = extension;
      }
    }
  }

  result += `.${max_extension}`;
  return result;
}



