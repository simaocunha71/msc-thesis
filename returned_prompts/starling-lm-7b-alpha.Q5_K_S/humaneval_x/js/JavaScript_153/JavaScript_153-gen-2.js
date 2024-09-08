  let result = class_name;
  let max_strength = 0;

  for (const ext of extensions) {
    let strength = 0;
    for (const c of ext) {
      if (c == c.toLowerCase()) {
        strength -= 1;
      } else {
        strength += 1;
      }
    }
    if (strength > max_strength) {
      result += `.${ext}`;
      max_strength = strength;
    }
  }

  return result;
}



