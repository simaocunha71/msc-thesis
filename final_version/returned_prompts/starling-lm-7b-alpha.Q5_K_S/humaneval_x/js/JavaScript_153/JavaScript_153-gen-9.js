  let result = class_name;
  let max_strength = 0;

  for (const e of extensions) {
    let strength = 0;
    for (const c of e) {
      if (c >= 'A' && c <= 'Z') {
        strength += 1;
      } else if (c >= 'a' && c <= 'z') {
        strength -= 1;
      }
    }
    if (strength > max_strength) {
      result = class_name + '.' + e;
      max_strength = strength;
    } else if (strength == max_strength && e < result.split('.')[1]) {
      result = class_name + '.' + e;
    }
  }

  return result;
}



